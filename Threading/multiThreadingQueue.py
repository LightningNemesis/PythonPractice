from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q, lock):
    while True:
        value = q.get()
        # simulating processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


# Idea:
# Each thread will pop 1 value from the queue

if __name__ == "__main__":
    numThreads = 10

    q = Queue()
    lock = Lock()

    for i in range(numThreads):
        thread = Thread(target=worker, args=(q, lock,))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("end main")
