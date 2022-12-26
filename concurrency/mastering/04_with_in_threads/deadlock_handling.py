from threading import Lock


def main():
    my_lock = Lock()
    data = []
    try:
        data, my_lock = get_data_from_file('./sample.txt', data, my_lock)
    except FileNotFoundError:
        print('File not found')
    my_lock.acquire()
    print(data)
    print('Lock can still be acquired')


def get_data_from_file(path, data, lock):
    lock.acquire()
    with open(path, 'r') as f:
        data.append(f.read())
    lock.release()
    return data, lock


if __name__ == '__main__':
    main()
