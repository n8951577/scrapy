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
cursor1 = db.cursor1()
# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET NAME='Paven' WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    cursor.execute('select * from employee')
    res = cursor.fetchall();
    print(res)
   # Commit your changes in the database
    db.commit()
except:
   # Rollback in case there is any error
    db.rollback()
db.close()
