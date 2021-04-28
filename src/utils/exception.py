import sys, os
import traceback
import functools


def exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            # raise Exception(f"exception: {e} - file_name: {traceback.extract_tb(exc_tb)[-1][0]} - line: {traceback.extract_tb(exc_tb)[-1][1]}")
            tb1 = traceback.TracebackException.from_exception(e)
            raise Exception(''.join(tb1.format()))
    return wrapper

