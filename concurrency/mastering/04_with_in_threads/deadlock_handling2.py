from threading import Lock


my_lock = Lock()
data = []


def get_data_from_file(filename):
    with my_lock, open(filename, 'r') as f:
        data.append(f.read())


try:
    get_data_from_file('myfile.txt')
except:
    print('Unexpected error')


my_lock.acquire()
print('Lock acquired.')
