#!/usr/bin/env python
import sys

__author__ = 'bogna'


class File_loader():

    def __init__(self, *args, **kwargs):
        """
        Init method for File_loader class
        :param args:
        :param kwargs:
        """
        if 'file' in kwargs.keys():
            self.file = kwargs.pop('file')
        self.read_file = []

    def open_and_read(self):
        """
        Open text file for both reading and writing
        """
        try:
            opened_file = open(self.file, mode="r")
        except IOError as e:
            print 'File {0} not found...'.format(self.file)
            sys.exit()

        for line in opened_file.readlines():
            self.read_file.append(line)


if __name__ == '__main__':
    File_loader()