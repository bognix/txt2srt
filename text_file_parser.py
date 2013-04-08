#!/usr/bin/env python

from mimetypes import guess_type
from subprocess import call, Popen, PIPE
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
        if not self.expected_format in guess_type(self.text_file):
            raise BadTypeException(
                'Expected format was {0} and format found was {1}'.format(
                    self.expected_format,
                    guess_type(self.text_file)[0]))

    def get_frames_from_txt_file(self):
        """Extract frames for each subtitle from text file"""
        self.frames = []
        for line in self.opened_file.readlines():
            self.frames.append(line.translate(None, "{").split("}")[:2])

    def get_frames_per_second(self, movie_file):
        """Get frame rate using mediainfo utility"""
        process = Popen(['mediainfo', movie_file], stdout=PIPE)
        result = process.communicate()[0].split("\n")
        fps = None
        for line in result:
            if "Frame rate" in line:
                fps = line.split(":")[1].translate(None, "")
        self.fps = fps.strip().split(" ")[0]

    def convert_from_frames_to_millis(self):
        """Using info about frame rate and frames extracted from text file
        convert frames to milliseconds"""





if __name__ == '__main__':
    Text_file_parser()

