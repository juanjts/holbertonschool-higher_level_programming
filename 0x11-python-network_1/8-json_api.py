#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    obj_req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        if len(obj_req.json()) == 0:
            print("No result")
        n_id = "[" + str(obj_req.json()['id']) + "]"
        n_name = obj_req.json()['name']
        print(n_id + " " + n_name)
    except ValueError:
        print("Not a valid JSON")
