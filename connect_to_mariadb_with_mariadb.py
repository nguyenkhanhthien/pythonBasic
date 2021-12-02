# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform


try:
    conn = mariadb.connect(
        user="select_api",
        password="some_pass",
        host="192.168.75.44",
        port=3306,
        database="cdrlog"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("select version()")
print(cur.fetchone())
conn.close()
