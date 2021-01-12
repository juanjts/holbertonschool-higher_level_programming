#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()
    acces_url = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    obj_req = requests.get(acces_url)
    com_list = obj_req.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                com_list[x].get("sha"),
                com_list[x].get("commit").get("author").get("name")))
    except:
        pass
