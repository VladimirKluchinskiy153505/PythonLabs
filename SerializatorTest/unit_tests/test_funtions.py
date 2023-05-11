import math
import re
import test_classes
k = 30
u = 40
first_class = test_classes.MyClass(4,8)
def sum(a,b):
    return a+b
def fact(n):
    if n <= 0:
        return 1
    else:
        return (n*fact(n-1))
def outer(n):
    my_class = test_classes.MyClass(3,5)
    def closure():
        nonlocal n
        global k
        global first_class
        a=20
        n+=10+ fact(7)
        n+=math.sin(n)+a+k+ + u + sum(2,3) + my_class.class_method()
        return n
    return closure
def decorator_square(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return new_function
@decorator_square
def new_sum(a, b):
    return a+b

def generator():
    while (True):
        yield 1
        yield 2
def sub_generator():
    while True:
        value = yield
        print('sub_generator recived value', value)

def main_generator():
    sub = sub_generator()
    next(sub)
    for i in range(5):
        sub.send('Hello')