import logging
logger1=logging.getLogger(__name__)
logger2=logging.getLogger("second_logger")
logger1.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(name)s:%(levelname)s:%(message)s")
file_handler1=logging.FileHandler("sample.log")

file_handler1.setFormatter(formatter)

logger1.addHandler(file_handler1)

stream_handler=logging.StreamHandler()
logger1.addHandler((stream_handler))
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(formatter)


def add(x,y):
    return x+y


def mul(x, y):
    return x * y


def div(x, y):
    try :
        r=x / y
    except ZeroDivisionError:
         logger1.exception("x divided by 0")
    else:
        return r





def sub(x, y):
    return x - y
x=10
y=0
n1=add(x,y)
logger1.debug(f"the sum of {x,y} is {n1}")
n2=mul(x,y)
logger1.debug(f"the multiplication of {x,y} is {n2}")
n3=sub(x,y)
logger2.debug(f"the subtraction of {x,y} is {n3}")
n4=div(x,y)
logger1.debug(f"the division  of {x,y} is {n4}")


