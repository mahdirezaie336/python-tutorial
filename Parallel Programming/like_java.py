from threading import Thread, Lock


lock = Lock()


def synchronized(f):
    def g(*args):
        lock.acquire()
        f(*args)
        lock.release()
    return g


a = 0


@synchronized
def f():
    global a
    for i in range(3000000):
        a += 1


number_of_threads = 2
t = [Thread(name=i, target=f) for i in range(number_of_threads)]
for i in range(number_of_threads):
    t[i].start()
for i in range(number_of_threads):
    t[i].join()

print(a)
