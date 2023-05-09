import inspect
import re

import unit_tests.test_classes as Classes


def create_class_point(name,bases,attrs):
    attrs.update({'Max_Cord': 100, 'Min_Cord': 0})
    return  type(name,bases, attrs)

class Point2D(metaclass= create_class_point):
     def get_coords(self):
         return (0,0)
class Meta(type):
    def __new__(cls, name, base, attrs): #метод вызываемый перед созданием класса
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)
    # def __init__(cls, name, base, attrs):
    #     #     super().__init__(name, base, attrs)
    #     #     cls.Max_COORD = 100
    #     #     cls.MIN_COORD = 0
# class Point3D:
#     def __init__(self,x,y):
#         self._x=x
#         self._y=y
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord)!= int:
#             raise TypeError('Coord must be int number')
#     @property
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self, coord):
#         self.verify_coord(coord)
#         self._x =coord
class Point(metaclass= Meta):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_coords(self):
        return(0,0)
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord)!= int:
            raise TypeError('Coord must be int number')

    def __set_name__(self,owner, name): #obj ref, class ref, prop_name in owner class
        self.name = '_' + name

    def __get__(self, instance, owner): #prop_ref, host_obj, class_obj
        return getattr(instance, self.name)
        #return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)
        #instance.__dict__[self.name] = value
class Point3D:
    x=Integer()
    y=Integer()
    z=Integer()
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == "__main__":
    # ClassType = type('Point',(),{'MaxX':100,'MaxY':200, 'method1': lambda self: self.MaxX + self.MaxY})
    # print(ClassType.mro())
    # obj = ClassType()
    # print(obj.method1())
    pt = Point3D(1,2,3)
    print(pt.__dict__, pt.z)
    obj = Classes.MyClass.method1
    if isinstance(obj, staticmethod):
        print('static')
    if isinstance(obj, classmethod):
        print('class_method')
    if inspect.ismethod(obj):
        print('method')
    if inspect.isfunction(obj):
        print('function')

    val = complex(4.2,-8.9)
    print(repr(val))

