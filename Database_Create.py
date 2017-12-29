import pymysql

# Open database connection
db = pymysql.connect(
        host='localhost',  # your host 
        user='root',       # username
        passwd='kiran',     # password
        db="TESTDB"       # name of the database
        )

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
res = cursor.fetchall()
print(res)

# disconnect from server
db.close()
