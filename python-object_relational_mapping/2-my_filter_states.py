#!/user/bin/python3
"""Display all values in the states table of hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":

    # Get MySQL credentials and search name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            host='localhost',
            port=3306)
    c = db.cursor()

    # Execute the SQL query to retrieve states with the specified name
    query = ("SELECT * FROM states "
             "WHERE name = '{}' ORDER BY id ASC".format(state_name)
            
    c.execute(query)

    # Fetch all rows and print the states
    rows = c.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    c.close()
    db.close()
