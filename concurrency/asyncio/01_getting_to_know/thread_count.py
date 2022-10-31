import os
import threading


print(f'Python process running with id {os.getpid()}')
n_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'Python currently running {n_threads} threads.')
print(f'Current thread is {thread_name}')
