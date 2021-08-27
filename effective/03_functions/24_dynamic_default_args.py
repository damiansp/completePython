from datetime import datetime
import json
from time import sleep
from typing import Optional


def log(msg, when=datetime.now()):
    print(f'{when}: {msg}')

log('Hi there!')
sleep(1)
log('Hello again!') # timestamps are identical


def log2(msg, when=None):
    '''
    Log message with timestamp
    Args:
      msg (str): message to log
      when (datetime): message time (defaults to present)
    '''
    if when is None:
        when = datetime.now()
    print(f'{when}: {msg}')


log2('Hi there!')
sleep(1)
log2('Hello again!') 


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo) # {'stuff': 5, 'meep': 1}
print('Bar:', bar) # {'stuff': 5, 'meep': 1}
assert foo is bar  # yup


def decode2(data, default=None):
    '''
    Load JSON from string
    Args:
      data (str): stingified JSON
      default: (json obj): value to return if decoding fails; default to {}
    '''
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
    return default


foo = decode2('bad data')
foo['stuff'] = 5
bar = decode2('also bad')
bar['meep'] = 1
print('Foo:', foo) # {'stuff': 5}
print('Bar:', bar) # {'meep': 1}
assert foo is not bar # ok


def log_typed(msg: str, when: Optional[datetime]=None) -> None:
    '''
    Log a message with a timestamp
    Args:
      msg (str): message to log
      when (datetime): message time (defaults to present)
    '''
    if when is None:
        when = datetime.now()
    print(f'{when}: {msg}')


log_typed('alas, it is over')
    
