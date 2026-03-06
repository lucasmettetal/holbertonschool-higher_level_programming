#!/usr/bin/python3
"""Print states starting with uppercase N."""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = connection.cursor()
    request = "SELECT * FROM states WHERE nameLIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(request)

    for item in cur.fetchall():
        print(item)

    cur.close()
    connection.close()
