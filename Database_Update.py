#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect(
        host='localhost',   
        user='root',       
        passwd='',     
        db="TESTDB"    
        )
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
db.close()
