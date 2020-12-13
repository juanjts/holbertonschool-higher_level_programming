#!/usr/bin/python3
"""Module documentation """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ main function """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
         ON states.id = cities.state_id WHERE states.name = %s", (argv[4], ))
    rows = cur.fetchall()
    string = ""
    for row in rows:
        string += str(*row) if string == "" else ", " + str(*row)
    print(string)
    cur.close()
    db.close()
