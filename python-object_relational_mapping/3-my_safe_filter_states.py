#!/user/bin/python3
"""Display values in the states table of hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":

    # Get the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = None

    try:
        # Connect to MySQL server
        db = MySQL.connect(
                user=mysql_username,
                passwd=mysql_password,
                db=database_name,
                host='localhost',
                port=3306)
        c = db.cursor()

        # Prepare SQL query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        c.execute(query, (state_name,))

        rows = c.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if db:
            db.close()
