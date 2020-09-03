#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    total = 0
    if count == 0:
        print(0)
    elif count == 1:
        print("{}".format(argv[1]))
    elif count > 1:
        for i in range(count):
            total = total + int(argv[i + 1])
        print("{}".format(total))
