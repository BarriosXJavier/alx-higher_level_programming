#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    The isinstance() function checks if the object is an instance of the specified class,
    or of a subclass of the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is a_class
