import mysql.connector
"""mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
#mycursor.execute("create database yamuna")
mycursor.execute("show databases")
for i in mycursor:
      print(i)"""

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="yamuna")
mycursor=mydb.cursor()
#mycursor.execute("create table teachers(sno int(10),name varchar(10),age int(10))")
mycursor.execute("show tables")
for i in mycursor:
      print(i)

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="yamuna")
mycursor=mydb.cursor()
sql=("insert into teachers(sno,name,age) values(%s,%s,%s)")
values=[(10,"uday",25),
        (11,"abhi",20),
        (12,"yamu",30)]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,"rows inserted")
a="select * from teachers"
mycursor.execute(a)
for i in mycursor:
            print(i)
      
     



