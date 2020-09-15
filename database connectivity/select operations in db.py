import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="aditidigital")
mycursor=mydb.cursor()

"""mycursor.execute("create table employee(sno varchar(10),name varchar(20),age integer(3))")
mycursor.execute("show tables")
for i in mycursor:
        print(i)"""

"""sql="insert into employee(sno,name,age) values(%s,%s,%s)"
values=(101,"abhi",21)
mycursor.execute(sql,values)
mydb.commit()
print(mycursor.rowcount,"record inserted")"""


sql="select * from crops"
mycursor.execute(sql)
for i in mycursor:
        print(i)

"""a = "SELECT * FROM crops where(area>=16000 and crop='rice')"
mycursor.execute(a)
for i in mycursor:
      print(i)"""
"""a="select crop,year,area from crops where(area>=2000 and crop='rice')"
mycursor.execute(a)
for i in mycursor:
        print(i)"""

"""a="select * from crops order by area desc"
mycursor.execute(a)
for i in mycursor:
        print(i)"""

"""a="select crop,sum(area) from crops group by crop"
mycursor.execute(a)
for i in mycursor:
        print(i)"""

"""a="select * from crops LIMIT 9 offset 7"
mycursor.execute(a)
for i in mycursor:
        print(i)"""
