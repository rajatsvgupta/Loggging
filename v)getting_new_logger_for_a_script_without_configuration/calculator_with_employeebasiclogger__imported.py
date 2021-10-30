import logging
import Employee_basic_with_logger

logging.basicConfig(filename="sample.log",level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

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
logging.debug(f"the sum of {x,y} is {n1}")
n2=mul(x,y)
logging.debug(f"the multiplication of {x,y} is {n2}")
n3=sub(x,y)
logging.debug(f"the subtraction of {x,y} is {n3}")
n4=div(x,y)
logging.debug(f"the division  of {x,y} is {n4}")


