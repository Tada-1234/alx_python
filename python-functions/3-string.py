#!/usr/bin/env python3
def reverse_string(string):
    length = len(string)
    new_string = str()
    while length > 0:
        new_string += string[length - 1]
        length = length - 1
    return new_string
