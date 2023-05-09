import my_xml_serializer
import my_json_serializer
import Functions
import Classes
if __name__ == '__main__':
    file_path = r'C:\Users\avdot\Desktop\page_xml2.txt'
    dict_obj = {'a': 3, 'b':3.698, 'c': complex(+3,+2), 'd': None, 'e': True, 'f': False}

    # with open(file_path, 'w') as file:
    #     my_xml_serializer.dump(obj, file)

    # obj3 = Classes.MyClass
    # print(obj3.class_method())
    # s1 = my_xml_serializer.dumps(obj3)
    # rest_obj = my_xml_serializer.loads(s1)
    # print(rest_obj.class_method())
    # print(rest_obj.static_method())

    # ser_dt = my_xml_serializer.dumps(obj2)
    # des_dt = my_xml_serializer.loads(ser_dt)
    # print(des_dt)
    #
    # ser_dt = my_json_serializer.dumps(obj2)
    # des_dt = my_json_serializer.loads(ser_dt)
    # print(des_dt)

    func = Functions.outer(10)
    print(func())
    print(func())
    print(func())
    ser_fc = my_xml_serializer.dumps(Functions.outer(10))
    des_fc = my_xml_serializer.loads(ser_fc)
    print('xml_ser')
    print(des_fc())
    print(des_fc())
    print(des_fc())
    ser_fc = my_json_serializer.dumps(Functions.outer(10))
    des_fc = my_json_serializer.loads(ser_fc)
    print('json_ser')
    print(des_fc())
    print(des_fc())
    print(des_fc())


