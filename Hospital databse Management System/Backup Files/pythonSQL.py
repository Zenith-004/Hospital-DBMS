import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="", database="db")
if mycon.is_connected():
    print("Successfully Conected to database")
else:
    print("Access denied")
cobj=mycon.cursor()
cobj.execute("select * from job")
data=cobj.fetchone()
count=cobj.rowcount
print("Total rows received:", count)
for row in data:
    print(row)
mycon.close()
