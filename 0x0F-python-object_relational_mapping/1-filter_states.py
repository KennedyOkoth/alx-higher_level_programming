#!/usr/bin/python3
"""Filters stste in a database accordin to letter N at the begining."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE LEFT(name, 1) = 'N' ORDER BY states.id")
    names = cur.fetchall()
    for name in names:
        print(name)

    cur.close()
    db.close()
