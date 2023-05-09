import math
class Person:
    position = "Student"
    __private_field = 'Adress'
    _protected_field = 'Number'
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def myname(self):
        print("Hello my name is " + self.name)

    def _myage(self):
        print("My age is " + self.age)
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age must be an integer')
        if value <0 or value >120:
            raise ValueError('Age must be between 0 and 120')
        self._age = value

    def __getattribute__(self, item):
       return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('__setattr__')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('__getattr__: '+ item)

    def __delattr__(self, item):
        print('__delattr__: '+item)
        object.__delattr__(self, item)

class Counter:
    def __init__(self):
        self.__counter =0
    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter +=1
        return self.__counter



def decorator_square(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return new_function

class MyClass:
    class_variable = 42

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @decorator_square
    def method1(self):
        return self.a + self.b

    @staticmethod
    def static_method():
        return "Hello, world!"

    @classmethod
    def class_method(cls):
        return cls.class_variable
def create_class_point(name,bases,attrs):
    attrs.update({'Max_Cord': 100, 'Min_Cord': 0})
    return type(name,bases, attrs)

class Point2D(metaclass= create_class_point):
     def get_coords(self):
         return (0,0)

class Meta(type):
    def __new__(cls, name, base, attrs): #метод вызываемый перед созданием класса
        attrs.update({'max_coord': 100, 'min_coord': 0, 'meta_method': cls.meta_method})
        return type.__new__(cls, name, base, attrs)
    @classmethod
    def meta_method(cls):
        return 777


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord)!= int:
            raise TypeError('Coord must be int number')

    def __set_name__(self,instance, name): #descriptor, instance, name of value in instance
        print('we are at set_name method, name is', name)
        self.name = 'prop_' + name

    def __get__(self, instance, instance_type=None): #descriptor object, parent object, class of instance
        return getattr(instance, self.name)
        #return instance.__dict__[self.name]

    def __set__(self, instance, value): #descriptor object, parent object, value
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)
        #instance.__dict__[self.name] = value

    def __delete__(self, instance):
        setattr(instance, self.name, None)
        print('delete was called')

class Point3D(metaclass= Meta):
    x = Integer()
    y = Integer()
    z = Integer()
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sum_coords(self):
        return self.x + self.y +self.z
    @classmethod
    def class_method(cls):
        return 'class method called'
    @staticmethod
    def static_method():
        return 'static_method called'

class Example(metaclass= Meta):
    def __init__(self, x):
        self.x =x

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def methodA(self):
        return math.sin(self.x) + math.cos(self.y)

class AA:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def methodAA(self):
        return math.tan(self.x) + math.cosh(self.y)

class B(A, AA):
    def __init__(self, x, y, a, b):
        A.__init__(self, x, y)
        AA.__init__(self, a, b)
    def methodB(self):
        return self.methodA() +self.methodAA()

