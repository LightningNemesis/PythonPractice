import functools


def repeat(num_times):
    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(0, num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Good Morning Mr. {name}")


greet("Nemesis")
