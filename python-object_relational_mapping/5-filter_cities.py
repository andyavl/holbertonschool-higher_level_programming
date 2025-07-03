#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa.
State name is passed as the fourth command-line argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]


    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    cities = cur.fetchall()

    print(", ".join(city[0] for city in cities))

    cur.close()
    db.close()
