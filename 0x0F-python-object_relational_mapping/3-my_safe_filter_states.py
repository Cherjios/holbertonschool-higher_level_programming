#!/usr/bin/python3
"""Sql injection """

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    pswd = sys.argv[2]
    dname = sys.argv[3]
    state_serch = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=pswd, db=dname, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC;",
                (state_serch,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
