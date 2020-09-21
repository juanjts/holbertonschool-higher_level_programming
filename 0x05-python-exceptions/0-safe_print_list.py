#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n_print = 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            n_print += 1
        print()
        return n_print
    except IndexError:
        print()
        return n_print
