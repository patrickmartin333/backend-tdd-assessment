#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Patrick Martin w/ help"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    # Creating initial parser
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    # Adding arguments to parser ('upper', 'lower', 'title' options)
    parser.add_argument("text", help="text to be manipulated")

    parser.add_argument("-u", "--upper", help="Convert text to uppercase",
                        action="store_true")
    parser.add_argument("-l", "--lower", help="Convert text to lowercase",
                        action="store_true")
    parser.add_argument("-t", "--title", help="Convert text to titlecase",
                        action="store_true")

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()  # Creates  parser instance
    x = parser.parse_args(args)
    result_text = x.text
    # if value is upper/lower/title
    if x.upper:
        result_text = result_text.upper()  # using uppercase method to convert text

    if x.lower:
        result_text = result_text.lower()  # using lowercase method to convert text

    if x.title:
        result_text = result_text.title()  # using .title method to convert text

    return result_text


if __name__ == '__main__':
    print(main(sys.argv[1:]))
