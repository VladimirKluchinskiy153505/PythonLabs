from kluchinskiy_serializer import great_serializer
#create serializer
json_serializer = great_serializer.create_serializer('json')
py_obj = {'a': 4.32, 'b': complex(2.4, -9.3), 'c':True}
#serialize object
ser_obj = json_serializer.dumps(py_obj)
#restore object
des_obj = json_serializer.loads(ser_obj)
print(des_obj)