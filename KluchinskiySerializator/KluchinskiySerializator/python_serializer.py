import types
import inspect
import re
from KluchinskiySerializator.consts_for_function import *
def serialize(object,cls =None):
    ser_dict = dict()
    object_type = type(object)
    #print('object_type',object_type)
    def object_type_name():
        return re.search(r"\'(\w+)\'", str(object_type))[1]

    if isinstance(object, (list, tuple, set, frozenset, bytearray, bytes)):
        ser_dict['type'] = object_type_name()
        ser_dict['value'] = [serialize(obj,cls) for obj in object]

    elif isinstance(object, (str, int, float, bool, complex)):
        ser_dict['type'] = object_type_name()
        ser_dict['value'] = object

    elif isinstance(object, dict): #dict
        ser_dict['type'] = object_type_name()
        ser_dict['value'] = [serialize([k, v]) for (k, v) in object.items()]

    elif inspect.isfunction(object): #function
        ser_dict['type'] = 'function'
        ser_dict['value'] = __serialize_function(object)
        #print(ser_dict)

    elif inspect.iscode(object): #code
        ser_dict['type'] = 'code'
        code_args_dict = dict()
        for (k, v) in inspect.getmembers(object):
            if k in CodeTypeArgs:
                code_args_dict[k] = serialize(v)
        ser_dict['value'] = code_args_dict

    elif isinstance(object, types.CellType): #cell
        ser_dict['type'] = 'cell'
        # print('cell_content', object.cell_contents)
        ser_dict['value'] = serialize(object.cell_contents, cls)

    elif inspect.isclass(object): #class
        ser_dict['type'] = 'class'
        if object!=cls:
            ser_dict['value'] = __serialize_class(object)
        else:
            # print('bases', object.__bases__)
            # print('bases[0]', object.__bases__[0])
            ser_dict['value'] = __serialize_class(object.__bases__[0])

    elif isinstance(object, property):
        ser_dict['type'] = 'property'
        ser_dict['value'] = __serialize_property(object)

    elif (not object): #None
        ser_dict['type'] = 'NoneType'
        ser_dict['value'] = None
    else:
        ser_dict['type'] = 'object'
        ser_dict['value'] = __serialize_object(object)
    return ser_dict
def __serialize_property(property_obj):
    # print('serialize_property')
    property_dict =dict()
    members = inspect.getmembers(property_obj)
    # print(members)
    for key,value in members:
        if key == 'fget' and value:
            property_dict['fget'] =__serialize_function(value)

        elif key == 'fset' and value:
            property_dict['fset'] = __serialize_function(value)

        elif key == 'fdel' and value:
            property_dict['fdel'] = __serialize_function(value)
    return property_dict
def __serialize_class(class_obj):
    class_dict = dict()
    class_dict['__name__'] = serialize(class_obj.__name__)
    # print(class_obj.__name__, '__dict__', class_obj.__dict__)
    # print('__bases__',class_obj.__bases__ )
    class_dict['__bases__'] = {'type': 'tuple', 'value': [serialize(base) for base in class_obj.__bases__ if base!= object]}
    for key in class_obj.__dict__:  # inspect.getmembers(obj):
        if (key in ("__name__", "__base__", "__basicsize__", "__dictoffset__", "__class__") or
                type(class_obj.__dict__[key]) in (
                        types.WrapperDescriptorType,
                        types.MethodDescriptorType,
                        types.BuiltinFunctionType,
                        types.GetSetDescriptorType,
                        types.MappingProxyType
                )):
            continue

        elif isinstance(class_obj.__dict__[key], staticmethod):
            class_dict[key] = {"type": "staticmethod",
                              "value": {"type": "function",
                                        "value": __serialize_function(class_obj.__dict__[key].__func__, class_obj)}}

        elif isinstance(class_obj.__dict__[key], classmethod):
            class_dict[key] = {"type": "classmethod",
                              "value": {"type": "function",
                                        "value": __serialize_function(class_obj.__dict__[key].__func__, class_obj)}}

        elif inspect.ismethod(class_obj.__dict__[key]):
            #class_dict[key] = {"type": "function", "value": serialize_function(class_obj.__dict__[key], class_obj)}
            class_dict[key] = {"type": "classmethod",
                               "value": {"type": "function",
                                         "value": __serialize_function(class_obj.__dict__[key], class_obj)}}

        elif inspect.isfunction(class_obj.__dict__[key]):
            class_dict[key] = {"type": "function", "value": __serialize_function(class_obj.__dict__[key], class_obj)}
        else:
            class_dict[key] = serialize(class_obj.__dict__[key])
    return class_dict
def __serialize_object(obj):
    object_dict = dict()
    object_dict['__class__'] = serialize(obj.__class__)
    members = dict()
    for k, v in inspect.getmembers(obj):
        if(k.startswith('__') or inspect.isfunction(v) or inspect.ismethod(v)):
            continue
        members[k] = serialize(v)
    object_dict['__members__'] = members
    return object_dict
def __serialize_function(func, cls = None):
    ser_value_func = dict()
    code_args_dict = dict()
    for (k,v) in inspect.getmembers(func.__code__):
        if k in CodeTypeArgs:
            code_args_dict[k] = serialize(v)

    ser_value_func['__code__'] = code_args_dict
    ser_value_func['__globals__'] = __get_globals_dict(func,cls)  # dict
    ser_value_func['__none_locals__'] = inspect.getclosurevars(func).nonlocals
    ser_value_func['__name__'] = func.__name__  # string
    if func.__defaults__:
        ser_value_func['__defaults__'] = serialize(func.__defaults__)  # tupple
    else:
        ser_value_func['__defaults__'] = serialize(tuple())  # tupple
    if func.__closure__:
        # print('func_closure', func.__closure__)
        ser_value_func['__closure__'] = serialize(func.__closure__,cls)  # tuple
    else:
        ser_value_func['__closure__'] = serialize(tuple())
   # print(ser_value_func)
    return ser_value_func
def __get_globals_dict(func, cls = None):
    globals_dict = dict()
    closurevars_dict = inspect.getclosurevars(func).globals
    for key in closurevars_dict:
        cl_object = closurevars_dict[key]
        if inspect.ismodule(cl_object):
            globals_dict['module ' + str(key)] = serialize(cl_object.__name__)

        elif inspect.isclass(cl_object):
            if(cls and cl_object != cls) or (not cls):
                print(cls)
                globals_dict[str(key)] = serialize(cl_object)

        elif key != func.__code__.co_name: #if name of object doesn't math name of function itself
            globals_dict[str(key)] = serialize(cl_object)
        else:
            globals_dict[key] = serialize(func.__name__)
    return globals_dict

def deserialize(obj: dict):
    if obj['type'] == 'NoneType':
        return None
    elif(obj["type"] in base_type):
        return __make_type(obj["type"], obj["value"])
    elif (obj["type"] in base_collection):
        return __make_collection(obj["type"], obj["value"])

    elif (obj["type"] == "dict"):
        return dict(__make_collection("list", obj["value"]))

    elif (obj["type"] == "function"):
        # print("type func value none", obj)
        return __deser_func(obj["value"])

    elif (obj["type"] == "code"):
        code = obj["value"]
        return types.CodeType(deserialize(code["co_argcount"]),
                              deserialize(code["co_posonlyargcount"]),
                              deserialize(code["co_kwonlyargcount"]),
                              deserialize(code["co_nlocals"]),
                              deserialize(code["co_stacksize"]),
                              deserialize(code["co_flags"]),
                              deserialize(code["co_code"]),
                              deserialize(code["co_consts"]),
                              deserialize(code["co_names"]),
                              deserialize(code["co_varnames"]),
                              deserialize(code["co_filename"]),
                              deserialize(code["co_name"]),
                              deserialize(code["co_qualname"]),
                              deserialize(code["co_firstlineno"]),
                              deserialize(code["co_linetable"]),
                              deserialize(code["co_lnotab"]),
                              deserialize(code["co_freevars"]),
                              deserialize(code["co_cellvars"]))
    elif (obj["type"] == "cell"):
        return types.CellType(deserialize(obj["value"]))

    elif (obj["type"] == "class"):
        return __deser_class(obj["value"])

    elif (obj["type"] == "staticmethod"):
        return staticmethod(deserialize(obj["value"]))

    elif (obj["type"] == "classmethod"):
        return classmethod(deserialize(obj["value"]))

    elif (obj["type"] == "object"):
        return __deser_object(obj["value"])

    elif (obj["type"] == "property"):
        return __deser_property(obj["value"])
def __deser_property(prop_object):
    fget = None
    fset =None
    fdel =None

    if 'fget' in prop_object:
        fget = __deser_func(prop_object['fget'])

    if 'fset' in prop_object:
        fset = __deser_func(prop_object['fset'])

    if 'fdel' in prop_object:
        fdel = __deser_func(prop_object['fdel'])
    return property(fget, fset, fdel)
def __make_type(_type, obj):
    if (_type == "int"):
        return int(obj)
    elif (_type == "float"):
        return float(obj)
    elif (_type == "complex"):
        return complex(obj)
    elif (_type == "str"):
        return str(obj)
    elif (_type == "bool"):
        return bool(obj)
def __make_collection(_type, obj):
    if (_type == "list"):
        return list(deserialize(item) for item in obj)
    elif (_type == "tuple"):
        return tuple(deserialize(item) for item in obj)
    elif (_type == "set"):
        return set(deserialize(item) for item in obj)
    elif (_type == "frozenset"):
        return frozenset(deserialize(item) for item in obj)
    elif (_type == "bytearray"):
        return bytearray(deserialize(item) for item in obj)
    elif (_type == "bytes"):
        return bytes(deserialize(item) for item in obj)
def __deser_func(obj):
    code = obj['__code__']
    globs = obj['__globals__']
    name = obj['__name__']
    argdefs = tuple(deserialize(obj['__defaults__']))
    closure = tuple(deserialize(obj['__closure__']))
    res_globs = dict()

    for k in obj["__globals__"]:
        if ("module" in k):
            res_globs[globs[k]["value"]] = __import__(globs[k]["value"])

        elif (globs[k] != obj["__name__"]):
            res_globs[k] = deserialize(globs[k])

    codeType = types.CodeType(deserialize(code["co_argcount"]),
                              deserialize(code["co_posonlyargcount"]),
                              deserialize(code["co_kwonlyargcount"]),
                              deserialize(code["co_nlocals"]),
                              deserialize(code["co_stacksize"]),
                              deserialize(code["co_flags"]),
                              deserialize(code["co_code"]),
                              deserialize(code["co_consts"]),
                              deserialize(code["co_names"]),
                              deserialize(code["co_varnames"]),
                              deserialize(code["co_filename"]),
                              deserialize(code["co_name"]),
                              deserialize(code["co_qualname"]),
                              deserialize(code["co_firstlineno"]),
                              deserialize(code["co_linetable"]),
                              deserialize(code["co_lnotab"]),
                              deserialize(code["co_freevars"]),
                              deserialize(code["co_cellvars"]))

    funcRes = types.FunctionType(codeType, res_globs, name, argdefs, closure)
    funcRes.__globals__.update({funcRes.__name__: funcRes})
    return funcRes
def __deser_class(obj):
    # print('class_obj_value', obj)
    bases = deserialize(obj["__bases__"])
    attrs = dict()
    for key, value in obj.items():
        attrs[key] = deserialize(value)
    class_obj = type(deserialize(obj["__name__"]), bases, attrs)
    return class_obj
def __deser_object(obj):
    class_obj = deserialize(obj["__class__"])
    members = dict()
    for k, v in obj["__members__"].items():
        members[k] = deserialize(v)
    res = object.__new__(class_obj)
    res.__dict__ = members
    return res