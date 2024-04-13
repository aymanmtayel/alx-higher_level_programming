#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time,it is safe from MySQL injections!"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cursor = data.cursor()
    QUERY = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
    statedata = cursor.execute(QUERY, (argv[4], ))
    for i in range(statedata):
        print(cursor.fetchone())
