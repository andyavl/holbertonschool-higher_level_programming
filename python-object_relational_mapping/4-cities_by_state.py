#!/usr/bin/python3
"""
Lists all cities in the database along with their corresponding state names,
ordered by cities.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]


    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()


    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)


    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
