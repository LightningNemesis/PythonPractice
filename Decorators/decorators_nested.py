
import functools


def header_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something first")
        func(*args, **kwargs)
        print("Something last")
    return wrapper


def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper


@header_decorator
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Lightning")
