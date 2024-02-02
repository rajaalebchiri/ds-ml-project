# using_gevent.py
import time
import gevent
from gevent import select

start = time.time()


def tic():
    return "at %1.1f seconds" % (time.time() - start)


def gr1():
    print("Started Polling: %s" % tic())
    select.select([], [], [], 2)
    print("Ended Polling: %s" % tic())


def gr2():
    print("Started Polling: %s" % tic())
    select.select([], [], [], 2)
    print("Ended Polling: %s" % tic())


def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)


def foo():
    print("Running in foo")
    gevent.sleep(1)
    print("Explicit context switch to foo again")


def bar():
    print("Explicit context to bar")
    gevent.sleep(1)
    print("implicit context switch back to bar")


gevent.joinall(
    [
        gevent.spawn(gr1),
        gevent.spawn(gr2),
        gevent.spawn(gr3)
    ]
)
