#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    sname = argv[4]
    cursor = data.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{:s}' ORDER BY id"
                   .format(sname))
    fetched = cursor.fetchall()
    for state in fetched:
        if state[1] == sname:
            print(state)
    cursor.close()
    data.close()
