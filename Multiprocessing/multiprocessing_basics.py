from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []  # List to store all my processes
num_processes = os.cpu_count()  # Good no. is CPU count on your machine

if __name__ == '__main__':
    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    # means: wait for a process to finish, while waiting block the main thread
    for p in processes:
        p.join()

    print('end main')
