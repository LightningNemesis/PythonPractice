from multiprocessing import Process, Value, Array, Lock, Queue
import os
import time


def squareNumbers(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def makeNegative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)


if __name__ == '__main__':
    numbers = range(1, 6)

    q = Queue()

    p1 = Process(target=squareNumbers, args=(numbers, q))
    p2 = Process(target=makeNegative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    print('end main')
