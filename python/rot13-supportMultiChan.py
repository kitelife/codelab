#-*- coding: utf-8 -*-

import sys
from optparse import OptionParser
import string

CHAR_MAP= dict(zip(
    string.ascii_lowercase,
    string.ascii_lowercase[13:26] + string.ascii_lowercase[0:13]
))

class RotateStream(object):
    '''
    General purpose ROT13 Translator

    A ROT13 translator smart enough to skip
    Markup tags if that's what we want.
    '''

    MARKUP_START = '<'
    MARKUP_END = '>'

    def __init__(self, skip_tags):
        self.skip_tags = skip_tags
    def rotate13_letter(self, letter):
        '''
        Return the 13-char rotation of a letter.
        '''
        do_upper = False
        if letter.isupper():
            do_upper = True
        letter = letter.lower()
        if letter not in CHAR_MAP:
            return letter
        else:
            letter = CHAR_MAP[letter]
            if do_upper:
                letter = letter.upper()
        return letter
    def rotate_from_file(self, handle):
        '''
        Rotate from a file handle

        Takes a file-like object and translates
        text from it into ROT13 text
        '''

        state_markup = False
        for line in handle:
            for char in line:
                if self.skip_tags:
                    if state_markup:
                        # here we're looking for a closing
                        # '>'
                        if char == self.MARKUP_END:
                            state_markup = False
                    else:
                        # Not in a markup state, rotate
                        # unless we're starting a new tag
                        if char == self.MARKUP_START:
                            state_markup = True
                        else:
                            char = self.rotate13_letter(char)
                else:
                    char = self.rotate13_letter(char)
                # Make this a generator
                yield char   #...
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-t', '--tags', dest='tags',
                      help='Ignore Markup Tags',
                      default = False,
                      action = 'store_true')  #...
    parser.add_option('-s', dest = 'selectInput',
                      default = False,
                      action = 'store_true')
    
    options, args = parser.parse_args()
    
    rotator = RotateStream(options.tags)
    if options.selectInput:
        for char in sys.argv[-1]:
            sys.stdout.write(rotator.rotate13_letter(char))
    else:
        for letter in rotator.rotate_from_file(sys.stdin):
            sys.stdout.write(letter)