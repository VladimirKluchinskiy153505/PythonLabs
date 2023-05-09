from KluchinskiySerializator import my_xml_serializer
from KluchinskiySerializator import my_json_serializer
def create_serializer(format:str):
    if format == ('json' or 'Json' or 'JSON'):
        return my_json_serializer
    elif format == ('xml' or 'Xml' or 'XML'):
        return my_xml_serializer
    else:
        return None

def convert_from_json_to_xml(json_obj:str):
    py_obj = my_json_serializer.loads(json_obj)
    xml_obj = my_xml_serializer.dumps(py_obj)
    return xml_obj

def convert_from_xml_to_json(xml_obj:str):
    py_obj = my_xml_serializer.loads(xml_obj)
    json_obj = my_json_serializer.dumps(py_obj)
    return json_obj

def convert_via_files(source_file, destination_file, source_format, destination_format):

    if (source_format == ('json' or 'Json' or 'JSON')) and (destination_format == ('xml' or 'Xml' or 'XML')):
        with open(source_file, 'r') as source:
            py_obj = my_json_serializer.load(source)
        with open(destination_file, 'w') as destination:
            my_xml_serializer.dump(py_obj, destination)

    elif (source_format == ('xml' or 'Xml' or 'XML')) and (destination_format == ('json' or 'Json' or 'JSON')):
        with open(source_file, 'r') as source:
            py_obj = my_xml_serializer.load(source)
        with open(destination_file, 'w') as destination:
            my_json_serializer.dump(py_obj, destination)

