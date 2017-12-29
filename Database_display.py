#Display the table data
#!/usr/bin/python
import pymysql

try:
    db = pymysql.connect(
        host='localhost',  # your host 
        user='root',       # username
        passwd='',     # password
        db="TESTDB"       # name of the database
        )

except Exception as e:
    sys.exit('we can;t get into the database')

cursor = db.cursor()
cursor.execute('SELECT * FROM employee')  #table name
result = cursor.fetchall()

print(result)



