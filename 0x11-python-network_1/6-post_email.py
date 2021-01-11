#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL
"""
import requests
import sys


if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)
