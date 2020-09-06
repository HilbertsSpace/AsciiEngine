#!/usr/bin/python

import sys

from ascii_generator import AsciiObject
from utils.exceptions import Error

ascii_funcs = ['help', 'generate_object']

def main():
    if sys.argv[1] == 'help':
        help()
    if sys.argv[1] in ascii_funcs and len(sys.argv) == 3:
        eval(sys.argv[1]+ '("' + sys.argv[2] + '")')

def generate_object(shape_function_input):
    try:
        new_ascii_object = AsciiObject(shape_function_input)
    except Error as e:
        print('Something went wrong. Could not create ascii '
              'generator from input: "{}". Reason: {}'.format(shape_function_input, e.message))

def help():
    print("You wanted help:")
    print("In order to run the Ascii engine, please use the command "
          "`generate_object` followed by your shape function")

if __name__ == "__main__":
    main()