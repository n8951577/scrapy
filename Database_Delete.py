import pymysql

db = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db = "TESTDB"
    )
cursor = db.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()


