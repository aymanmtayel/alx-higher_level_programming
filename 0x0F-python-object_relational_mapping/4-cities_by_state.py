#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    QUERY = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    data_r = cursor.execute(QUERY)
    for i in range(data_r):
        print(cursor.fetchone())
    cursor.close()
    conn.close()
