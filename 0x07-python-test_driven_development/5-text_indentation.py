#!/usr/bin/python3
"""
Module
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    for j, l in enumerate(text):
        if l in ['.', '?', ':']:
            print(text[i:j + 1].strip() + '\n')
            i = j + 1
    print(text[i:].strip(), end='')
