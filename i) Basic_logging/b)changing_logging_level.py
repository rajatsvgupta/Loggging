import logging
def add(x,y):
    """Add function"""
    return(x+y)
def sub(x,y):
    """sub function"""
    return(x-y)
def div(x,y):
    """divide function"""
    return(x/y)
def mul(x,y):
    """multiply function"""
    return(x*y)
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=10)
a=10
b=5
add_result=add(a,b)
logging.debug(f"Add: {a} + {b}={add_result}")
sub_result=sub(a,b)
logging.debug(f"sub: {a} - {b}={sub_result}")
div_result=div(a,b)
logging.debug(f"div: {a} / {b}={div_result}")
mul_result=mul(a,b)
logging.debug(f"mul: {a} * {b}={mul_result}")
