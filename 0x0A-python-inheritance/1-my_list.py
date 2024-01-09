#!/usr/bin/python3

"""module to print list in an ascending order"""

class MyList(list):
    """ The list class """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
