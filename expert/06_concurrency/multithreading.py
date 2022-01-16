from threading import Lock, Thread


def my_func():
    print('printing from thread!')


thread_visits = 0
more_visits = 0
more_visits_lock = Lock()


def visit_counter():
    global thread_visits
    for i in range(100_000):
        val = thread_visits
        thread_visits = val + 1


def locking_visit_counter():
    global more_visits
    for i in range(100_000):
        with more_visits_lock:
            more_visits += 1
        

if __name__ == '__main__':
    thread = Thread(target=my_func)
    thread.start()
    thread.join()

    print('\nPart Two:')
    threads = [Thread(target=my_func) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print('\nPart Three:')
    n = 100
    threads = [Thread(target=visit_counter) for _ in range(n)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'{n=}, {thread_visits=}')

    print('\nPart Four:')
    n = 100
    threads = [Thread(target=locking_visit_counter) for _ in range(n)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'{n=}, {more_visits=}')
