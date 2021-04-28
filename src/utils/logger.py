import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} input {kwargs}")
        value = func(*args, **kwargs)
        print(f"output {value} from {func.__name__}")
        return value
    return wrapper