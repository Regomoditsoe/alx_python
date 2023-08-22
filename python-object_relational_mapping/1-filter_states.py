#!user/bin/python3
"""List all states with a name starting with N from database hbtn_0e_0_usa."""
import sys
import MySQLdb


if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments

    # Connect to MySQL server
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    c.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch and print results
    states = c.fetchall()
    for state in states:
        print(state)

    # Close database
    db.close()
