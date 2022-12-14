#!/usr/bin/python3
"""
    a script that takes in an argument and
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = db_con.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s ORDER
                BY states.id ASC""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db_con.close()
