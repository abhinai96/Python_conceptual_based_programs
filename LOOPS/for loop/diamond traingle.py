n=int(input("enter no of rows:"))
for i in range(1,n+1):
        for j in range(i,n+1):
                print(" ",end="")
        for z in range(1,i+1):
                print("*",end=" ")
        print()
        j-=1
