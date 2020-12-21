#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Prototype function to find peak of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    for i in range(0, len(list_of_integers)):
        peak = list_of_integers[0]
        if i == len(list_of_integers) - 1:
            break
        if list_of_integers[i] > list_of_integers[i + 1]\
                and list_of_integers[i] > list_of_integers[i - 1]:
            peak = list_of_integers[i]
            break
    return peak
