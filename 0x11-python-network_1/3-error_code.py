#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response
"""


import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    obj_req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(obj_req) as openf_req:
            print(openf_req.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
