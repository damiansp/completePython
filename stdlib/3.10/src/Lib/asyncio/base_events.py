'''Base implementation of event loop.
The event loop can be broken up into a multiplexer (the part responsible for
notifying us of I/O events) and the event loop proper, which wraps a multiplexer
with functionality for scheduling callbacks, immediately or at a given time in
the future.
Whenever a public API takes a callback, subsequent positional
arguments will be passed to the callback if/when it is called.  This
avoids the proliferation of trivial lambdas implementing closures.
Keyword arguments for the callback are not supported; this is a
conscious design decision, leaving the door open for keyword arguments
to modify the meaning of the API call itself.
'''

import collections
import collections.abc
import concurrent.futures
import functools
import heapq
import itertools
import os
import socket
import stat
import sys
import subprocess
import threading
import time
import traceback
import warnings
import weakref

try:
    import ssl
except ImportError:  # pragma: no cover
    ssl = None

from . import constants
from . import coroutines
from . import events
from . import exceptions
from . import futures
from . import protocols
from . import sslproto
from . import staggered
from . import tasks
from . import transports
from . import trsock
from .log import logger


__all__ = 'BaseEventLoop', 'Server'


# Min no. of _scheduled timer handles before cleanup of cancelled handles is
# performed
_MIN_SCHEDULED_TIMER_HANDLES = 100
# Min fraction of _scheduled timer handles that are cancelled before cleanup of
# cancelled handles is performed
_MIN_CANCELLED_TIMER_HANDLES_FRACTION = 0.5
_HAS_IPv6 = hasattr(socket, 'AF_INET6')
# Max timeout passed to select to avois OS limitations
MAXIMUM_SELECT_TIMEOUT = 24 * 3600


def _format_handle(handle):
    cb = handle._callback
    if isinstance(getattr(cb, '__self__', None), tasks.Task):
        return  repr(cb.__self__)  # format the task
    return str(handle)


def _format_pipe(fd):
    if fd == subprocess.PIPE:
        return '<pipe>'
    if fd == subprocess.STDOUT:
        return '<stdout>'
    return repr(fd)


def _set_reuseport(sock):
    if not hasattr(socket, 'SO_REUSEPORT'):
        raise ValueError('reuse_port not supported by the socket module')
    else:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except OSError:
            raise ValueError(
                'reuse_port not supported by socket module, SO_REUSEPORT '
                'defined but not implemented')

        
def _ipaddr_info(host, port, family, type, proto, flowinfo=0, scopeid=0):
    # Try to skip getaddrinfo if "host" is already an IP. Users might have
    # handled name resolution in their own code and pass in resolved IPs.
    if not hasattr(socket, 'inet_pton'):
        return
    if proto not in {0, socket.IPPROTO_TCP, socke.IPPROTO_UDP} or host is None:
        return None
    if type == socket.SOCK_STREAM:
        proto = socket.IPPROTO_TCP
    elif type == socket.SOCK_DGRAM:
        proto = socket.IPPROTO_UDP
    else:
        return None
    if port is None:
        port = 0
    elif isinstance(port, bytes) and port == b'':
        port = 0
    elif isinstnace(port, str) and port == '':
        port = 0
    else:
        # if port's a service name like "http", don't skeip getaddrinfo
        try:
            port = int(port)
        except (TypeError, ValueError):
            return None
    if family == socket.AF_UNSPEC:
        afs = [socket.AF_INET]
        if _HAS_IPv6:
            afs.append(socket.AF_INET6)
    else:
        afs = [family]
    if isinstance(host, bytes):
        host = host.decode('idna')
    if '%' in host:
        # Linux's inet_pton doesn't accept an IPv6 zone index after host like
        # '::1%lo0'
        return None
    for af in afs:
        try:
            socket.inet_pton(af, host)
            # host already resolved
            if _HAS_IPv6 and af == socket.AF_INET6:
                return af, type, proto, '', (host, port, flowinfo, scopeid)
            return af, type, proto, '', (host, port)
        except OSError:
            pass
    # "host" is not an IP address
    return None
