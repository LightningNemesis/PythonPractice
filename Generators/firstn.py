import sys


def firstn(n):
    nums = []
    num = 0
    while (num < n):
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while (num < n):
        yield num
        num += 1


myList = firstn(10)
# sumList = sum(myList)
# print(myList, sumList)

# print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
