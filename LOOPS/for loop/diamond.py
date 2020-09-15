a=5
for i in range(1,a+1):
        for j in range(5,i,-1):
                print("",end=" ")
        for z in range(1,i+1):
                print("*",end=" ")
        print()
for x in range(1,a+1):
        for y in range(1,x+1):
                print("",end=" ")
        for b in range(a,x,-1):
                print("*",end=" ")
        print()
