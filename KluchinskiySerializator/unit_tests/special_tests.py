import inspect
import kluchinskiy_serializer
from kluchinskiy_serializer import great_serializer
import tests.unit_tests.test_classes
import python_serializer
class Parent1:
    def __init__(self, value1):
        self.value1 = value1
class Parent2:
    def __init__(self, value2):
        self.value2 = value2

class Child(Parent1, Parent2):
    def __init__(self, value1, value2, value3):
        Parent1.__init__(self, value1)
        Parent2.__init__(self, value2)
        self.value3 = value3

if __name__ == '__main__':
    # point = test_classes.Point3D(1, 2, 3)
    # print(point.meta_method())
    # class_obj = test_classes.Point3D
    # print('_dict_', class_obj.__dict__)
    # print('members', inspect.getmembers(class_obj))
    # ser_obj = python_serializer.serialize(class_obj)
    # print('ser_obj', ser_obj)
    # des_obj = python_serializer.deserialize(ser_obj)

    # example = test_classes.Example
    # print(example.meta_method())
    # print('dict', example.__dict__)
    # print('members', inspect.getmembers(example))
    # ser_class = python_serializer.serialize(example)
    # print(ser_class)
    # des_class = python_serializer.deserialize(ser_class)
    # print(des_class.meta_method())
    # child = Child(1, 2, 3)
    # new_class = test_classes.B
    # obj = new_class(1,2,3,4)
    # print(test_classes.Person.__dict__)
    # print(test_classes.Person._protected_field)
    # print(test_classes.Person._Person__private_field)
    # person = test_classes.Person('Igor', 'Voitenko')
    # person.age = 23
    # print(person.height)
    c =test_classes.Counter()
    c()
    c()
    c()
    c()
    print(c())
    json_serializer = great_serializer.create_serializer('json')
    ser_obj = json_serializer.dumps(c)
    obj = json_serializer.loads(ser_obj)
    print(obj())
