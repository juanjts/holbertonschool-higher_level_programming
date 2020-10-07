#!/usr/bin/python3
"""add attr module"""


def add_attribute(obj, attribute, value):
    """add an attribute"""

    if '__dict__' not in dir(obj) or '__slots__' in dir(obj):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attribute, value)
