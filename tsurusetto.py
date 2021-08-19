#!/bin/env python3
# 2 Enter space betweeen similar functions/conversives of each other
# 4 Enter space betweeen 2 different functions
# A comment line to specify what it does.


def character_to_ascii(character_series):
    '''Converts a characterstring to ascii numbers'''
    ascii_series = [" ".join(str(ord(characters)) for characters in character_series)][0]
    return ascii_series


def ascii_to_character(ascii_series):
    character_series = "".join([" ".join(str(chr(int(characters)))) for characters in ascii_series.split(' ')])

    return character_series



test = ascii_to_character(character_to_ascii("hello world"))
print(test)
