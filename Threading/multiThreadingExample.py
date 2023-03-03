from threading import Thread, Lock
import time


# Objectives:
# 1. Create 2 threads
# 2. Assign same target function to each thread -> to modify a global variable
# 3. Observe what happens when both threads finish executing -> Does the variable value get changed? How many times?
# 4. Introduce "Lock" and then go to step 3 again

# Represents a DB that each thread can perform an operation on
databaseValue = 0


# Without context manager
def increaseValue(lock):
    global databaseValue

    lock.acquire()
    # Simulating: Processing on the DB
    localCopy = databaseValue
    localCopy += 1
    time.sleep(0.1)

    databaseValue = localCopy
    lock.release()


# With context manager
def increaseValueContext(lock):
    global databaseValue

    with lock:
        # Simulating: Processing on the DB
        localCopy = databaseValue
        localCopy += 1
        time.sleep(0.1)

        databaseValue = localCopy


if __name__ == "__main__":
    print(f"Start value: {databaseValue}")

    lock = Lock()
    # Create 2 threads
    # thread1 = Thread(target=increaseValue, args=(lock,))
    # thread2 = Thread(target=increaseValue, args=(lock,))

    thread1 = Thread(target=increaseValueContext, args=(lock,))
    thread2 = Thread(target=increaseValueContext, args=(lock,))

    # Starting both threads
    thread1.start()
    thread2.start()

    # Waiting for both threads to finish
    thread1.join()
    thread2.join()

    print(f"End value: {databaseValue}")
    print("end main")
