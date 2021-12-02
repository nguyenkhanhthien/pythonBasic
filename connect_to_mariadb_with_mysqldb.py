#!/usr/bin/env python3
import MySQLdb
# Create db connection
db = MySQLdb.connect(host="x.x.x.x", port=3306, user="xxxx", passwd="xxxx", db="xxxx")
# To perform a query, you first need a cursor
c = db.cursor()
# make select version query
c.execute("select version()")
# Print output of the query
print(c.fetchone())
db.close()
