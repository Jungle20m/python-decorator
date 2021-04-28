import traceback

from src.utils.exception import exception
from src.utils.timer import timer
from src.utils.logger import logger


@exception
def sub_1():
    raise Exception("error from sub_1")

# @exception
def sub_2():
    print("hello from sub 2")

@exception
def function1():
    sub_1()
    sub_2()

# @exception
def function2():
    pass
    
# @exception
def function3():
    pass
    

# @exception
def main():
    function1()
    function2()
    function3()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)