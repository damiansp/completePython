from datetime import datetime
from time import sleep


def log(msg, when=datetime.now()):
    print(f'{when}: {msg}')

log('Hi there!')
sleep(2)
log('Hello again!') # timestamps are identical


