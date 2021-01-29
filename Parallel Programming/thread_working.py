from threading import Thread
from functions import *


def start_and_join(t):
    for i in t:
        i.start()
    for i in t:
        i.join()


def solve():
    t = [Thread(name=(i+1), target=f[i]) for i in range(4)]
    start_and_join(t)
    t = [Thread(name=(i+1), target=g[i]) for i in range(2)]
    start_and_join(t)
    t = [Thread(name=1, target=h[0])]
    start_and_join(t)


solve()
