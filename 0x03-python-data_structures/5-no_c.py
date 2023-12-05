#!/usr/bin/python3
def no_c(my_string):
    result_str = ""

    for char in my_string:
        if char.lower() != 'c':
            result_str += char
        return result_str
