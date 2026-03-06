#!/usr/bin/python3
"""Print all states starting with uppercase N."""

import MySQLdb
import sys


def main():
    """Connect to the database and display matching states."""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
