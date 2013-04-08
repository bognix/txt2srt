#!/usr/bin/env python
from file_loader import File_loader
from text_file_parser import Text_file_parser
import argparse

__author__ = 'bogna'


def main():
    """Main function - runs program and parses arguments"""

    parser = argparse.ArgumentParser('Convert txt file to srt file')
    media_parser = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument('-i', '--input_txt_file', dest='text_file',
                        action='store', required=True,
                        help='Path to the text file you want to \
                        convert to srt')
    parser.add_argument('-o', '--output_file', dest='output_file',
                        action='store', required=False,
                        help='Optional path to the output srt file, \
                        by default current path, file name same as txt file')

    media_parser.add_argument('--movie', dest='movie', action='store_true')
    media_parser.add_argument('--fps', action='store_true')

    args, unknown = parser.parse_known_args()

    if args.text_file:
        file_parser = Text_file_parser(text_file=args.text_file)
        file_parser.open_file()
        file_parser.check_text_file()
        file_parser.get_frames_from_txt_file()
        file_parser.get_frames_per_second(unknown[0])



if __name__ == '__main__':
    main()

