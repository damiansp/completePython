import os
import json
from getpass import getpass
from mysql.connector import connect, Error


HOME = os.environ['HOME']
KEYS = f'{HOME}/config/keys.json'


def main():
    user, password = get_keys()
    is_successful = connect_test(user, password)
    print('Successful:', is_successful)
    

def get_keys():
    with open(KEYS, 'r') as f:
        keys = json.load(f)['mySQL']
    user = keys['username']
    password = keys['password']
    return user, password


def connect_test(user, password):
    try:
        with connect(host='localhost', user=user, password=password) as conn:
            print(conn)
        return True
    except Error as e:
        print(e)
        return False


if __name__ == '__main__':
    main()

