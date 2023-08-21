#!user/bin/python3
"""List all states with a name starting with N from database hbtn_0e_0_usa."""
import sys
import MySQLdb


if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database)
    c = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    c.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%  ORDER BY `id`")

    # Fetch and print results
    states = c.fetchall()
    for state in states:
        print(state)

    # Close database
    db.close
