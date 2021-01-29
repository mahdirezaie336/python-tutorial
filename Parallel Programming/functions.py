import threading


def func():
    print(threading.current_thread().name, 'is running...')


f = [func, func, func, func]
g = [func, func]
h = [func]
