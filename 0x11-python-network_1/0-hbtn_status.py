#!/usr/bin/python3
""" script that fetches an url"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as open_file:
    """Open the URL, which can be either a string or a Request object."""
    read_file = open_file.read()
    """
    read content from Reques object or string passed from url request.
    second print: show contenent in read_file
    last print: show decode contenet with utf-8
    """
    print('Body response:')
    print("\t- type: {}".format(type(read_file)))
    print("\t- content: {}".format(read_file))
    print("\t- utf8 content: {}".format(read_file.decode('utf-8')))
