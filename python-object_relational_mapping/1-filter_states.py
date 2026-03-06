#!/usr/bin/python3
"""List all states from the database."""

import MySQLdb
import sys


def main():
    """Run the SQL query and print results."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC;
        """)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
