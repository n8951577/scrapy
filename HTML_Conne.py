import pymysql
try:
    print("<html<head>")
    print("<Script typ=\"text/javascript \">function showSchemaName(o) {")
    print("alert('You have selected ' + o.value);")
    print(" } </script></head>")
    print("<body>")
    print("<h1> Connecting to PySQL...")
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        port=3306,
        db="TESTDB"
    )
    cursor=conn.cursor()
    cursor.execute("select distinct table_schema from information_schema.tables order by 1")
    print("Select database Schema:")
    print("<select id=\"abc\" onchange=\"showSchemaName(this)\">")
    for row in cursor:
        print("<option" + row[0] + "</option")
    print("</select>")
    print("connection succedded")
    print("</body></html>")
except:
    print("Connection failed")


import datetime
hai=datetime.datetime.today()
print(hai)