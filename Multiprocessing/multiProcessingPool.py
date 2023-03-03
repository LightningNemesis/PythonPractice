from multiprocessing import Process, Pool


def cube(number):
    return number*number*number


if __name__ == "__main__":
    pool = Pool()

    numbers = range(10)

    # map, apply, join, close
    result = pool.map(cube, numbers)
    # result = pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
