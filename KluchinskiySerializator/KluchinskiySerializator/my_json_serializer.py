from KluchinskiySerializator import python_serializer
import regex
int_pattern = r"(?<!\.)\s*(?:[\+-]?\d+)\b(?![\.])" #1
float_pattern = r"(?:[+-]?\d+\.\d+)\b" #1
complex_pattern = r"(?:\([-]?\d+(?:[\.]\d+)?[+-]\d+(?:[\.]\d+)?j\))" #1
bool_pattern = r"\b(?:true|false)\b" #1
str_pattern = r"(?:\"[^\"]*\")" #1
none_pattern = r"\b(?:None)\b" #1
list_pattern = r"\[(?:[^\[\]]|(?R))*\]"
dict_pattern = r"\{(?:[^{}]|(?R))*\}"
obj_pattern = fr"({int_pattern}|{float_pattern}|{complex_pattern}|{bool_pattern}|{str_pattern}|{none_pattern}|{list_pattern}|{dict_pattern})"
def dumps(py_obj):
    ser_obj_dict = python_serializer.serialize(py_obj)
    #print('ser_obj_dict',ser_obj_dict)
    ser_obj_json = __con_to_json(ser_obj_dict)
    #print('ser_obj_json', ser_obj_json)
    return ser_obj_json
def loads(json_obj:str):
    deser_obj_dict = __des_from_json(json_obj)
    #print('des_from_json', deser_obj_dict)
    py_obj = python_serializer.deserialize(deser_obj_dict)
    return py_obj
def dump(py_obj, file):
    file.write(dumps(py_obj))
def load(file):
    return loads(file.read())
def __con_to_json(obj):
    if isinstance(obj,dict): #dict
        delimiter = ', '
        return '{'+delimiter.join([ f"{__con_to_json(key)}: {__con_to_json(obj[key])}" for key in obj]) + '}'

    elif isinstance(obj,list): #list
        delimiter = ', '
        return '[' + delimiter.join([__con_to_json(item) for item in obj]) + ']'

    elif isinstance(obj,(bool)): #bool
        if obj == True:
            return "true"
        else:
            return "false"
    elif isinstance(obj, (int, float, complex)):  # int
        return str(obj)

    elif isinstance(obj,str):
        return '"' + obj + '"'
def __des_from_json(str_obj:str):
    str_obj = str_obj.strip()
    match = regex.fullmatch(int_pattern, str_obj)
    if match:
        return int(match.group(0))

    match = regex.fullmatch(float_pattern, str_obj)
    if match:
        return float(match.group(0))

    match = regex.fullmatch(complex_pattern, str_obj)
    if match:
        return complex(match.group(0))

    match = regex.fullmatch(bool_pattern, str_obj)
    if match:
        return match.group(0) == 'true'

    match = regex.fullmatch(str_pattern, str_obj)
    if match:
        s1 = match.group(0)
        return s1[1:-1]

    match = regex.fullmatch(none_pattern, str_obj)
    if match:
        return match.group(0) == 'None'

    if str_obj.startswith('[') and str_obj.endswith(']'):
        list_objects = regex.findall(obj_pattern, str_obj[1:-1])
        #print('list_oj', list_objects)
        return [__des_from_json(match) for match in list_objects]

    if str_obj.startswith('{') and str_obj.endswith('}'):
        new_str = str_obj[1:-1]
        dict_objects = regex.findall(obj_pattern, new_str)
        #print('dict_obj', dict_objects)
        return {__des_from_json(dict_objects[i]): __des_from_json(dict_objects[i+1]) for i in range(0, len(dict_objects)-1, 2)}

