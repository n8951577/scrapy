import pymysql
db = pymysql.connect(
    host='localhost',  # your host 
        user='root',       # username
        passwd='',     # password
        db="TESTDB"       # name of the database
        )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()
