#!/usr/bin/python3
# Lsiting all states from data base hbtn_0e_0_usa

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    pssw = sys.argv[2]
    datab_name = sys.argv[3]

    datab = MySQLdb.connect(host="localhost", port=3306, user=username,
                            passwd=pssw, db=datab_name, charset="utf8")
    cur = datab.cursor()
    cur.execute("SELECT * FORM state ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    datab.close()
