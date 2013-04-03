#!/usr/bin/env python
from file_loader import File_loader
from text_file_parser import Text_file_parser
import argparse

__author__ = 'bogna'


def main():
    """Main function - runs program and parses arguments"""

    parser = argparse.ArgumentParser('Convert txt file to srt file')
    parser.add_argument('-i', '--input_txt_file', dest='text_file',
                        action='store', required=True,
                        help='Path to the text file you want to \
                        convert to srt')
    parser.add_argument('-o', '--output_file', dest='output_file',
                        action='store', required=False,
                        help='Optional path to the output srt file, \
                        by default current path')

    args = parser.parse_args()

    if args.text_file:
        file_parser = Text_file_parser(text_file=args.text_file)
        file_parser.open_file()
        file_parser.check_text_file()



if __name__ == '__main__':
    main()

