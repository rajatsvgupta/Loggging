import logging
import employee_modified
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter("%(name)s:%(levelname)s:%(message)s")
file_handler=logging.FileHandler("sample.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def add(x,y):
    return x+y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def sub(x, y):
    return x - y
x=10
y=5
n1=add(x,y)
logger.debug(f"the sum of {x,y} is {n1}")
n2=mul(x,y)
logger.debug(f"the multiplication of {x,y} is {n2}")
n3=sub(x,y)
logger.debug(f"the subtraction of {x,y} is {n3}")
n4=div(x,y)
logger.debug(f"the division  of {x,y} is {n4}")


