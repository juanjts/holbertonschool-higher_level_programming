#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    obj_req = requests.get(sys.argv[1])
    code = obj_req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    print(obj_req.text)
