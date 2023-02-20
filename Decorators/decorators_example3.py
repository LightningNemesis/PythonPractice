
import functools


def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper


@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Lightning")
