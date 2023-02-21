# Generators: Functions which generate iterable objects (as and when required)
# PROs: Memory efficient

def myGenerator():
    yield 3
    yield 2
    yield 1


g = myGenerator()

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# print(sum(g))
print(sorted(g))
