# Similar to Higher Order Functions

# @myDecorator
# def doSomething():
#     pass

import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # Arguments, Keyword Arguments
        # Do something before...
        result = func(*args, **kwargs)
        # Do something After...
        return result
    return wrapper


@start_end_decorator
def add5(x):
    return x+5


print(add5(10))

# print_name = start_end_decorator(print_name)
# print_name()

# result = add5(10)
# print(help(add5))
# print(add5.__name__)
