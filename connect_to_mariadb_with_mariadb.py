#mysql> CREATE USER 'select_api'@'localhost' IDENTIFIED BY 'some_pass';
#mysql> GRANT ALL PRIVILEGES ON *.* TO 'select_api'@'localhost' WITH GRANT OPTION;
#mysql> CREATE USER 'select_api'@'%' IDENTIFIED BY 'some_pass';
#mysql> GRANT ALL PRIVILEGES ON *.* TO 'select_api'@'%' WITH GRANT OPTION;

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform


try:
    conn = mariadb.connect(
        user="xxx",
        password="xxx",
        host="xxx",
        port=3306,
        database="xxx"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("select version()")
print(cur.fetchone())
conn.close()
