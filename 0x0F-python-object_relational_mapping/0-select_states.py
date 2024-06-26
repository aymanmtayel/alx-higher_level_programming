#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cursor = data.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    data.close()
