#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_d = number % -10
else:
    l_d = number % 10
if l_d > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l_d))
elif l_d == 0:
    print("Last digit of {} is {} and is 0".format(number, l_d))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".
        format(number, l_d))
