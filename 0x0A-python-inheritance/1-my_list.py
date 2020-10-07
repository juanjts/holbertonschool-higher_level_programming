#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
