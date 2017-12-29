import mysql.connector as conn

#connect to server
db=conn.connect(host="localhost",user="root",password="")
cursor=db.cursor()
#create database
#cursor.execute("""CREATE DATABASE IF NOT EXISTS Testdb""")
#db.commit()
#use database
#create student table
cursor.execute("""CREATE TABLE IF NOT EXISTS Student(
    StudentNo INT PRIMARY KEY,
    StudentSurname TEXT,
    StudentForename TEXT,
    StudentTeacher VARCHAR(255),
    StudentPassword TEXT)""")
db.commit()
#create exam tabledb.commit()
db.commit()
cursor.close()     
