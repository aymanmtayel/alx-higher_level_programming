#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    QUERY = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s ORDER BY cities.id"
    data_r = cursor.execute(QUERY, (argv[4], ))
    data = cursor.fetchall()
    output = [city[0] for city in data]
    print(", ".join(output))
    cursor.close()
    conn.close()
