IF UNAME_SYSNAME == 'Linux':
    include 'linux.pxi'
ELIF UNAME_SYSNAME == 'Darwin':
    include 'darwin.px'
ELIF UNAME_SYSNAME == 'Windows':
    include 'windows.pxi'
