from KluchinskiySerializator import python_serializer
import regex
int_pattern = r"<int>\w+<\/int>"
float_pattern = r"<float>[-]?\w+\.\w+<\/float>"
complex_pattern = r"<complex>\(.+\)<\/complex>"
bool_pattern = r"<bool>(?:True|False)<\/bool>"
str_pattern = r"<str>(?:.*?)<\/str>"
none_pattern = r"<NoneType>None</NoneType>"
list_pattern = r"<list>(?P<content>(?:(?!<list>|<\/list>).|(?R))*)<\/list>"
dict_pattern = r"<dict>(?P<content>(?:(?!<dict>|<\/dict>).|(?R))*)<\/dict>"
obj_pattern = fr"({int_pattern}|{float_pattern}|{complex_pattern}|{bool_pattern}|{str_pattern}|{none_pattern}|{list_pattern}|{dict_pattern})"
complex_value_pattern = r"(\([-]?\d+(?:[\.]\d+)?[+-]\d+(?:[\.]\d+)?j\))"
def dumps(py_obj):
    ser_obj_dict = python_serializer.serialize(py_obj)
    #print('ser_obj_dict',ser_obj_dict)
    ser_obj_xml = __con_to_xml(ser_obj_dict)
   #print('ser_obj_xml', ser_obj_xml)
    return ser_obj_xml

def dump(py_obj,file):
    file.write(dumps(py_obj))
def loads(xml_obj):
    deser_obj_dict = __des_from_xml(xml_obj)
    #print('des_from_xml', deser_obj_dict)
    py_obj = python_serializer.deserialize(deser_obj_dict)
    return py_obj

def load(file):
    return loads(file.read())

def __con_to_xml(py_obj):
    if isinstance(py_obj,bool):
        return '<bool>'+str(py_obj)+'</bool>'
    elif isinstance(py_obj,int):
        return '<int>'+str(py_obj)+'</int>'

    elif isinstance(py_obj,float):
        return '<float>'+str(py_obj)+'</float>'

    elif isinstance(py_obj,complex):
        return '<complex>'+str(py_obj)+'</complex>'

    elif isinstance(py_obj,str):
        return '<str>'+py_obj+'</str>'

    elif isinstance(py_obj,list):
        delimiter = ''
        return '<list>'+delimiter.join([__con_to_xml(o) for o in py_obj])+'</list>'

    elif isinstance(py_obj, dict):
        singles = [item for pair in py_obj.items() for item in pair]
        delimiter = ''
        return '<dict>'+delimiter.join([__con_to_xml(item) for item in singles])+'</dict>'

    else:
        return '<NoneType>None</NoneType>'
def __des_from_xml(xml_obj:str):
    xml_obj = xml_obj.strip()
    match = regex.fullmatch(int_pattern, xml_obj)
    if match:
        int_val = regex.search(r"(\d+)", xml_obj).group(1)
        return int(int_val)

    match = regex.fullmatch(float_pattern, xml_obj)
    if match:
        float_val = regex.search(r"([-]?\d+\.\d+)", xml_obj).group(1)
        return float(float_val)

    match = regex.fullmatch(complex_pattern, xml_obj)
    if match:
        complex_val = regex.search(complex_value_pattern, xml_obj).group(1)
        return complex(complex_val)

    match = regex.fullmatch(bool_pattern, xml_obj)
    if match:
        bool_val = regex.search(r"(True|False)", xml_obj).group(1)
        return bool_val == 'True'

    match = regex.fullmatch(str_pattern, xml_obj)
    if match:
        str_val = regex.search(r">(.+)<", xml_obj).group(1)
        return str_val

    match = regex.fullmatch(none_pattern, xml_obj)
    if match:
        return None

    match = regex.fullmatch(list_pattern, xml_obj)
    if match:
        list_objects = regex.findall(obj_pattern, xml_obj[1:-1])
        #print('list_obj:', list_objects)
        return [__des_from_xml(item[0]) for item in list_objects]

    match = regex.fullmatch(dict_pattern, xml_obj)
    if match:
        dict_objects = regex.findall(obj_pattern, xml_obj[1:-1])
        #print('dict_obj:', dict_objects)
        return {__des_from_xml(dict_objects[i][0]) : __des_from_xml(dict_objects[i+1][0]) for i in range(0, len(dict_objects)-1, 2)}
