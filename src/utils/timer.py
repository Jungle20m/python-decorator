import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"finished {func.__name__} in: {duration:.4f}")
        return value
    return wrapper