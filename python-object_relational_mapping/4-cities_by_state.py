#!/use/bin/python3
"""List all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and search name from command line args
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            host='localhost',
            port=3306)
    c = db.cursor()

    # Execute SQL query to retrieve all states
    query = ("SELECT c.id, c.name, s.name "
                "FROM cities as c "
                "INNER JOIN states as s "
                "ON c.state_id = s.id "
                "ORDER BY c.id")
    c.execute(query)

    # Fetchall rows and print cities
    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connections
    c.close()
    db.close()
