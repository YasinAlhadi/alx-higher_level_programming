#!/usr/bin/python3
"""
    a script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if len(sys.argv) > 3:
    db_con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = db_con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_con.close()
