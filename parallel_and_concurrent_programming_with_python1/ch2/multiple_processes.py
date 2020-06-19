import os
import threading
import multiprocessing as mp

def cpu_waster():
    while True:
        pass


print('Hi! My name is', __name__)
if __name__ == '__main__':
    print('\n Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)


    print('\nStarting 12 CPU Wasters...')
    for i in range(12):
        mp.Process(target=cpu_waster).start()

    print('\n Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)
