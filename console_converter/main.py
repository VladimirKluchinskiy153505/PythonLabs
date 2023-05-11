from KluchinskiySerializator import great_serializer
import objects.test_objects
import objects.test_classes
if __name__ == '__main__':
    # xml_serializer = great_serializer.create_serializer('xml')
    # with open('files/xml.txt', 'w') as file:
    #     xml_serializer.dump(objects.test_objects.dict_obj, file)

    json_serializer = great_serializer.create_serializer('json')
    with open('files/json2.txt', 'w') as file:
        json_serializer.dump(objects.test_classes.PropHolder, file)