#!/usr/bin/python
"""Parses EITI excel data into JSON and CSV files"""

import os.path
import parse
import json
from pprint import pprint
# import sys


def main():
# def main(args):
    """main body"""

    json_data = []

    root_dir = os.path.dirname(os.path.realpath(__file__))

    for (source_dir, dir_list, file_list) in os.walk(root_dir):
        if dir_list == ['.git', 'output']:
            for file_name in file_list:
                if ".xlsx" in file_name:
                	parse.main(file_name, json_data)
    # pprint(json_data)
    # write out json 
	print_out = open('output/eiti.json', 'w')
	print_out.write(json.dumps(json_data, indent=4, separators=(',', ':')))

	print_out.close()

if __name__ == '__main__':
    main()
