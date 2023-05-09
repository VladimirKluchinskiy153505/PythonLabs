import argparse
from KluchinskiySerializator import great_serializer
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converting formats')
    parser.add_argument('input_file', metavar='<file_from>', help='input file')
    parser.add_argument('output_file', metavar='<file_to>', help='output file')
    parser.add_argument('input_format', metavar='<format_from>', help='input format')
    parser.add_argument('output_format', metavar='<format_to>', help='output format')
    args = parser.parse_args()
    great_serializer.convert_via_files(args.input_file, args.output_file, args.input_format, args.output_format)