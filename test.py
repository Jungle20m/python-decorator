import traceback


def stack_lvl_3():
    raise Exception('a1', 'b2', 'c3')


def stack_lvl_2():
    try:
        stack_lvl_3()
    except Exception as e:
        # raise
        return e


def stack_lvl_1():
    e = stack_lvl_2()
    return e

e = stack_lvl_1()

tb1 = traceback.TracebackException.from_exception(e)
print(''.join(tb1.format()))