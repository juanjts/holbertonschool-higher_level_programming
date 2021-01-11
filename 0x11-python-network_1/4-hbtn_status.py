#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    obj_req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: " + str(type(obj_req.text)))
    print("\t- content: " + obj_req.text)
