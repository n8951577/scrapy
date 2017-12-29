#!/usr/bin/python
import pymysql

# Open database connection
db = pymysql.connect(
        host='localhost',  # your host 
        user='root',       # username
        passwd='',     # password
        db="TESTDB"       # name of the database
        )

cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (10000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      FIRST_NAME = row[0]
      LAST_NAME = row[1]
      AGE = row[2]
      SEX = row[3]
      INCOME = row[4]

      # Now print fetched result
      print('fname=%s,lname=%s,age=%d,sex=%s,income= %d') % \
           (fname, lname, age, sex, income )
except:
   print ("Error: unable to fecth data")

db.close()
