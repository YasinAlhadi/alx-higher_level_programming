#!/usr/bin/python3
"""
    a script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("""SELECT name FROM cities WHERE state_id = (SELECT id
                FROM states WHERE name = %s)
                ORDER BY id ASC""", (sys.argv[4],))
    rows = cur.fetchall()
    q_list = []
    for row in rows:
        q_list.append(row[0])
    _str = ", ".join(q_list)
    print(_str)
    cur.close()
    db_con.close()
