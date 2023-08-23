#!/user/bin/python3
"""Display all values in the states table of hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":

    # Get MySQL credentials and search name from command line arguments
    # and # Connect to MySQL server
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306)
    c = db.cursor()

    state_name = sys.argv[4]

    # Execute the SQL query to retrieve states with the specified name
    query = ("SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id ASC ".format(state_name))

    # Fetch all rows and print the states
    rows = c.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor
    c.close()

    # Close database
    db.close()
