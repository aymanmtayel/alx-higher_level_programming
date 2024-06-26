#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cursor = data.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
    cursor.close()
    data.close()
