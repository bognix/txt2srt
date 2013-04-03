#!/usr/bin/env python
import mimetypes
from FileParsingErrors import BadTypeException

__author__ = 'bogna'


class Text_file_parser():
    def __init__(self, *args, **kwargs):
        """
        Initialize Text_file_parser object. Load, check and parse text file.
        :param kwargs:
        """
        if 'text_file' in kwargs.keys():
            self.text_file = kwargs.pop('text_file')
        self.expected_format = "text/plain"

    def open_file(self):
        try:
            self.opened_file = open(self.text_file, 'r')
        except IOError as e:
            raise IOError('File {0} not found'.format(self.text_file))

    def check_text_file(self):
        """Check if loaded file is a correct text file"""
        if not self.expected_format in mimetypes.guess_type(self.text_file):
            raise BadTypeException(
                'Expected format was {0} and format found was {1}'.format(
                    self.expected_format,
                    mimetypes.guess_type(self.text_file)[0]))


if __name__ == '__main__':
    Text_file_parser()

