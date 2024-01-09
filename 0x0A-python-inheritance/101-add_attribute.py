#!/usr/bin/python3

def add_attribute(obj, attr, value):
    if not isinstance(obj, (int, float, str, bytes, bool, type(None))):
        setattr(obj, attr, value)
    else:
        raise TypeError('can\'t add new attribute')

