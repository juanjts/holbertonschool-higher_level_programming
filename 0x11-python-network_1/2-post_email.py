#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL"""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    e_value = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    obj_req = urllib.request.Request(url, data)
    with urllib.request.urlopen(obj_req) as openf_req:
        r_content = openf_req.read()
        print(r_content.decode("utf-8"))
