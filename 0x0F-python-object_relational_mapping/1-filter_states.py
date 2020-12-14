#!/usr/bin/python3
"""Module documentation """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ main function """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT states.name FROM states WHERE name\
         LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
