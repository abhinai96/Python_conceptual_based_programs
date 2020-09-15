lst=[]

b=int(input("enter no of rows "))
c=int(input("enter no of colums"))
for i in range(b):
        m=[]
        for j in range(c):
                a=int(input("enter the numbers:"))      
                m.append(a)
        lst.append(m)
        
        print(lst)



import numpy as np
e=np.array([lst])
print("the matrix from user input is shown below")

print(e)


