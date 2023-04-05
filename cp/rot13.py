#-*- coding: utf-8 -*-
import sys
import string

CHAR_MAP = dict(zip(
    string.ascii_lowercase,
    string.ascii_lowercase[13:26] + string.ascii_lowercase[0:13]
))

def rotate13_letter(letter):
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

if __name__ == '__main__':
    for char in sys.argv[1]:
        sys.stdout.write(rotate13_letter(char))
    sys.stdout.write('\n')