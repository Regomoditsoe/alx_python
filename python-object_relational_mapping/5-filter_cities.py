#!/user/bin/python3
"""Take a stake as an argument and list all cities of the state"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    ddatabase_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            host='localhost',
            port=3306)
    c = db.cursor()

    # Execute the SQL queryto retrieve cities
    query = ("SeLeCT * FROM cities as c "
             "INNER JOIN states as s "
             "ON c.state_id = s.id "
             "WHERE s.name = %s "
             "ORDER BY c.id ASC")
    c.execute(query, (state_name,))

    # Fetch all rows and print cities separated by commas
    cities = [ct[2] for ct in c.fetchall()]
    print(", ".join(cities))

    # Close cursor and database connection
    c.close()
    db.close()
