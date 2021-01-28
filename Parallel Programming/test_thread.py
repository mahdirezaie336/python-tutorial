import threading
import time


def f(i):
    print('Thread', i, 'has started.')
    time.sleep(5)
    print('Thread', i, 'finished.')


for i in range(4):
    threading.Thread(target=f, args=(i, )).start()
    time.sleep(0.5)
