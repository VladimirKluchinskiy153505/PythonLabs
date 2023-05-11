from dataclasses import dataclass
from functools import reduce
import unit_tests.test_classes as Classes
import gc
@dataclass
class Person:
    name: str
    age: int
    email: str = None

def sub_generator():
    while True:
        value = yield
        print('sub_generator recived value', value)

def main_generator():
    sub = sub_generator()
    next(sub)
    for i in range(5):
        sub.send('Hello')
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}:{self.name}"

    def __str__(self):
        return f"{self.name}"
def generator1(start, end):
    for i in range(start, end):
        yield i

class Goods:
    def __int__(self,name, weight, price):
        super().__init__()
        print('init googs')
        self.name = name
        self.weight = weight
        self.price = price
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class MixingLog:
    ID = 0
    def __init__(self):
        print('init MixingLog')
        self.ID +=1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00")

class NoteBook(Goods, MixingLog):
    pass
if __name__ == '__main__':
    p = Person('Alice', 30)
    cat = Cat('Vasia')
    print(repr(cat))
    print(str(cat))
    lt = [x**2 if x>0 else x**3 for x in range(-10,10) if x%2 == 0]
    print(lt)
    p = Classes.Point(1,-2, -9)
    print(len(p))
    print(abs(p))
    print((lambda a, b: a*b)(17, 14))
    print((lambda a,b: a if a >b else b)(25,14))
    numbers = [1, 2, 3, 4, 5]
    squares = map(lambda x: x ** 2, numbers)
    print(list(squares))  # [1, 4, 9, 16, 25]
    numbers = [1, 2, 3, 4, 5]
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))  # [2, 4]

    numbers =[1, 2, 3, 4, 5]
    sum = reduce(lambda x,y:x+y,numbers)

    ls = (x**2 for x in range(1000000))
    # print(next(ls))
    # print(next(ls))
    # print(next(ls))

    gen = generator1(1,3)
    print(next(gen))
    print(next(gen))
    print(Cat.__mro__)


