#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    """
    do a request about url and print X-Request-Id value, it is in
    the header of response(obejct Request)
    """

    obj_req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(obj_req) as openf_req:
        print(openf_req.getheader('X-Request-Id'))
