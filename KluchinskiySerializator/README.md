from KluchinskiySerializator import great_serializer
#
xml_serializer = great_serializer.create_serializer('xml')
ser_func = xml_serializer.dumps(func)
des_func = xml_serializer.loads(ser_func)
#
des_func()