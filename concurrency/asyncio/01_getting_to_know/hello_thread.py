import threading


def main():
    hello_thread = threading.Thread(target=hello)
    hello_thread.start()
    n_threads = threading.active_count()
    thread_name = threading.current_thread().name
    print(f'Python running {n_threads} threads')
    print(f'Current thread is {thread_name}')
    hello_thread.join()

    
def hello():
    print(f'Hello forom thread {threading.current_thread()}!')


if __name__ == '__main__':
    main()

