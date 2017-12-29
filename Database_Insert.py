import pymysql

# Open database connection
db = pymysql.connect(
        host='localhost',  # your host 
        user='root',       # username
        passwd='kiran',     # password
        db="TESTDB"       # name of the database
        )

cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Kiran', 'Sokki', 25, 'M', 20000)"""
try:
   cursor.execute(sql)
   db.commit()

except:
   db.rollback()

# disconnect from server
db.close()


# Video reference for connecting a DATABASE In PYMYSQL
# https://www.youtube.com/watch?v=4Y5zjTJ9LV4