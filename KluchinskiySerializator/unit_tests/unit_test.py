import unittest
import test_funtions
import test_objects
import test_classes
from KluchinskiySerializator import great_serializer
class TestFunction(unittest.TestCase):
    def test_function(self):
        func = test_funtions.outer(10)
        json_serializer = great_serializer.create_serializer('json')
        ser_func = json_serializer.dumps(func)
        des_func = json_serializer.loads(ser_func)
        self.assertEqual((func(), func(), func()), (des_func(), des_func(), des_func()))

    def test_function1(self):
        func = test_funtions.fact
        xml_serializer = great_serializer.create_serializer('xml')
        ser_func = xml_serializer.dumps(func)
        des_func = xml_serializer.loads(ser_func)
        self.assertEqual((func(5), func(10), func(15)), (des_func(5), des_func(10), des_func(15)))

    def test_function2(self):
        func = test_funtions.new_sum
        xml_serializer = great_serializer.create_serializer('xml')
        ser_func = xml_serializer.dumps(func)
        des_func = xml_serializer.loads(ser_func)
        self.assertEqual(func(3, 5), des_func(3, 5))

    def test_function3(self):
        func = test_funtions.generator
        json_serializer = great_serializer.create_serializer('json')
        ser_gen = json_serializer.dumps(func)
        des_gen = json_serializer.loads(ser_gen)
        self.assertEqual((next(func()), next(func()), next(func())), (next(des_gen()), next(des_gen()), next(des_gen())))

class TestSimpleObjects(unittest.TestCase):
    def test(self):
        obj = test_objects.dict_obj
        xml_serializer = great_serializer.create_serializer('xml')
        ser_obj = xml_serializer.dumps(obj)
        des_obj = xml_serializer.loads(ser_obj)
        self.assertEqual(obj, des_obj)

    def test1(self):
        obj = (7.25, complex(-3.35, -9.999), [1, True, [1, complex(1, 2.5), {'a': 3, 'b': ['qwert', 7]} ]])
        json_serializer = great_serializer.create_serializer('json')
        ser_obj = json_serializer.dumps(obj)
        des_obj = json_serializer.loads(ser_obj)
        self.assertEqual(obj, des_obj)

class TestClassObjects(unittest.TestCase):
    def test(self):
        obj = test_classes.MyClass(2, 7)
        xml_serializer = great_serializer.create_serializer('xml')
        ser_obj = xml_serializer.dumps(obj)
        des_obj = xml_serializer.loads(ser_obj)
        self.assertEqual((obj.method1(), obj.class_method(), obj.static_method()), (des_obj.method1(), des_obj.class_method(), des_obj.static_method()))

    def test1(self):
        obj = test_classes.Point3D(1, 2, 3)
        print(obj.__dict__)
        print(obj.max_coord)
        print(obj.meta_method())
        json_serializer = great_serializer.create_serializer('json')
        ser_obj = json_serializer.dumps(obj)
        des_obj = json_serializer.loads(ser_obj)
        print(des_obj.__dict__)
        self.assertEqual((obj.max_coord, obj.min_coord, obj.sum_coords(), obj.meta_method()), (des_obj.max_coord, des_obj.min_coord, des_obj.sum_coords(), des_obj.meta_method()))

    def test_inheritance(self):
        obj = test_classes.B
        xml_serializer = great_serializer.create_serializer('xml')
        ser_obj = xml_serializer.dumps(obj)
        des_obj = xml_serializer.loads(ser_obj)
        print(obj(1, 2, 3, 4))
        self.assertEqual(obj(1, 2, 3, 4).methodB(), des_obj(1,2,3,4).methodB())

    def test_call(self):
        obj = test_classes.Counter()
        obj()#1
        obj()#2
        xml_serializer = great_serializer.create_serializer('xml')
        ser_obj = xml_serializer.dumps(obj)
        des_obj = xml_serializer.loads(ser_obj)
        self.assertEqual(des_obj(), 3)

    def test_property(self):
        obj = test_classes.PropHolder(23, 1, 3)
        xml_serializer = great_serializer.create_serializer('xml')
        ser_obj = xml_serializer.dumps(obj)
        des_obj = xml_serializer.loads(ser_obj)
        obj.Age =500
        des_obj.Age = obj.Age
        self.assertEqual((des_obj.Age, des_obj.method1()),(obj.Age, obj.method1()))

    def test_hard_inheritance(self):
        my_bat = test_classes.Bat("Dracula", "Megachiroptera", 2, 10)
        json_serializer = great_serializer.create_serializer('json')
        ser_obj = json_serializer.dumps(my_bat)

        des_obj = json_serializer.loads(ser_obj)
        # Call some methods
        self.assertEqual((my_bat.give_birth(), my_bat.lay_eggs(), my_bat.fly()), (des_obj.give_birth(), des_obj.lay_eggs(), des_obj.fly()))

if __name__ == '__main__':
    unittest.main()