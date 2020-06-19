import os
import threading

def cpu_wasters():
    while True:
        pass


print('\n Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)


print('\n Starting 12 CPU wasters..')
for i in range(12):
    threading.Thread(target=cpu_wasters).start()

print('\n Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)
