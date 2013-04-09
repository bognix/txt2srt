#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from mimetypes import guess_type
from subprocess import Popen, PIPE
from FileParsingErrors import BadTypeException

__author__ = 'bogna'


class Text_To_Srt_Converter():
    def __init__(self, *args, **kwargs):
        """
        Initialize Text_file_parser object. Load, check and parse text file.
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
        """
        Check if loaded file is a correct text file
        """
        if not self.expected_format in guess_type(self.text_file):
            raise BadTypeException(
                'Expected format was {0} and format found was {1}'.format(
                    self.expected_format,
                    guess_type(self.text_file)[0]))

    def get_subs_from_txt_file(self):
        """
        Extract frames for each subtitle from text file
        """
        self.subtitles = []
        for line in self.opened_file.readlines():
            subs_line = line.translate(None, "{").split("}")
            subs_line[-1] = subs_line[-1].replace("|", "\n").replace("\r", "")
            subs_line[-1] = subs_line[-1].decode("windows-1250").encode('utf-8')
            self.subtitles.append(subs_line)

    def get_frames_per_second(self, movie_file):
        """
        Get frame rate using mediainfo utility
        """
        process = Popen(['mediainfo', movie_file], stdout=PIPE)
        result = process.communicate()[0].split("\n")
        fps = None
        for line in result:
            if "Frame rate" in line:
                fps = line.split(":")[1].translate(None, "")
        self.fps = fps.strip().split(" ")[0]

    def convert_from_frames_to_millis(self):
        """
        Using info about frame rate and frames extracted from text file
        convert frames to milliseconds
        """
        k = 0
        for subtitle_set in self.subtitles:
            i = 0
            for frame in subtitle_set[:2]:
                time_in_millis = (float(frame) / float(self.fps)) * 1000
                subtitle_set[i] = self.convert_from_millis(time_in_millis)
                i += 1
            self.subtitles[k] = subtitle_set
            k += 1

    def convert_from_millis(self, milliseconds):
        """
        Convert time given in millis to readable format: HH:MM:SS:mmm.
        Thank you Sven Marnach from stack overflow for this suggestion :)
        """
        hours, milliseconds = divmod(milliseconds, 3600000)
        minutes, milliseconds = divmod(milliseconds, 60000)
        seconds = float(milliseconds) / 1000
        return "%02i:%02i:%06.3f" % (hours, minutes, seconds)

    def create_srt_file(self):
        f = open('out.srt', 'w')
        for i in range(1, len(self.subtitles) + 1):
            j = i-1
            single_sub = self.subtitles[j]
            srt_single_sub = "%s\n%s --> %s\n%s\n"\
                             % (i, single_sub[0], single_sub[1], single_sub[2])
            f.write(srt_single_sub)
        f.close()

