def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(5)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
