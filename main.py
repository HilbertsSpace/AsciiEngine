#!/usr/bin/python

import argparse
import sys

from ascii_generator import AsciiObject
from utils.exceptions import Error
from config import DEFAULT_BOUNDING_BOX, DEFAULT_STEP_SIZE, DEFAULT_ROTATION_AXIS

ascii_funcs = ['help', 'generate_object']

def main():
    parser = argparse.ArgumentParser(description="Generate an Ascii based 3D object based on input function.")
    # Set the default for the dataset argument
    parser.add_argument(
        "--func",
        nargs="?",
        help="Enter a mathematical equation that will represent your shape.",
        required = True,
        type=str,
    )
    parser.add_argument(
        "--rotation_axis",
        nargs="?",
        default=DEFAULT_ROTATION_AXIS,
        type=str,
        help="The axis which the user's func will be rotated to generate the object."
    )
    parser.add_argument(
        "--x_bound",
        type=list,
        default=DEFAULT_BOUNDING_BOX,
        help="The bounding box for x values in the user's func. Defaults to [10, 10]"
    )
    parser.add_argument(
        "--y_bound",
        type=list,
        default=DEFAULT_BOUNDING_BOX,
        help="The bounding box for y values in the user's func. Defaults to [10, 10]"
    )
    parser.add_argument(
        "--step_size",
        type=int,
        default=DEFAULT_STEP_SIZE,
        help="Step size for the user's func. Defaults to 1"
    )
    args = parser.parse_args()
    # Create a dictionary of the shell arguments

    kwargs = vars(args)
    ascii_object = AsciiObject(**kwargs)

if __name__ == "__main__":
    main()