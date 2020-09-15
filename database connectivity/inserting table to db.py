import mysql.connector
""""mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="ibm")
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE employee(sno varchar(10),name varchar(20),age integer(3))")
mycursor.execute("CREATE TABLE teacherdata(sno varchar(10),name varchar(20),age integer(3))")
mycursor.execute("show tables")
for i in mycursor:
        print(i)"""


mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="ibm")
mycursor=mydb.cursor()

sql="INSERT INTO employee(sno,name,age)VALUES(%s,%s,%s)"
values=[("101","abhi",21),
        ("201","shiva",25),
        ("304","teja",30)]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,"records inserted")
a="SELECT * From employee"
mycursor.execute(a)
for i in mycursor:
        print(i)


