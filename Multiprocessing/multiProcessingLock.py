from multiprocessing import Process, Value, Array, Lock
import os
import time

# Race condition: Multiple threads or processes try to modify a common variable at the same time


# def add100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1

def add100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for j in range(len(numbers)):
                numbers[j] += 1


if __name__ == '__main__':

    lock = Lock()

    sharedNumber = Value('i', 0)
    sharedArray = Array('d', [0.0, 100.0, 70.0])

    # print(f"Number at the start is {sharedNumber.value}")
    print(f"Array at the start is {sharedArray[:]}")

    # p1 = Process(target=add100, args=(sharedNumber, lock))
    # p2 = Process(target=add100, args=(sharedNumber, lock))
    p1 = Process(target=add100, args=(sharedArray, lock))
    p2 = Process(target=add100, args=(sharedArray, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # print(f"Value at the end is {sharedNumber.value}")
    print(f"Array at the start is {sharedArray[:]}")

    print('end main')
