#!/usr/bin/python3
""" Find peak in unsorted integers """


def find_peak(list_of_integers):
    """Prototype function used to find a peak of integers"""

    if len(list_of_integers) == 0:
        return None
    argvs = list_of_integers
    leng = len(list_of_integers)
    peak = leng // 2
    if (peak == leng - 1 or argvs[peak] >= argvs[peak + 1]):
        if (peak == 0 or argvs[peak] >= argvs[peak - 1]):
            return argvs[peak]
    if peak != leng - 1 and argvs[peak + 1] > argvs[peak]:
        return find_peak(argvs[peak + 1:])
    return find_peak(argvs[:peak])
