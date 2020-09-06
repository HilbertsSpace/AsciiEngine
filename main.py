#!/usr/bin/python

import sys

ascii_funcs = ['help', 'generate_object']

def main():
    if sys.argv[1] == 'help':
        help()
    if sys.argv[1] in ascii_funcs and len(sys.argv) == 3:
        eval(sys.argv[1]+ '("' + sys.argv[2] + '")')

def generate_object(input):
    print("this was your input: {}".format(input))

def help():
    print("You wanted help")

if __name__ == "__main__":
    main()