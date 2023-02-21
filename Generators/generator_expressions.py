import sys

myGenerator = (i for i in range(100000) if i % 2 == 0)
print(sys.getsizeof(myGenerator))

myList = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(myList))
