l=6
h=8
for i in range(1,l+1):
        print("*",end=" ")
print()
for z in range(1,h-1):
        for k in range(0,l):
                if k==0:
                        print("*",end=" ")
                elif k==l-1:
                        print("*",end=" ")
                else:
                        print(" ",end=" ")
        print()
                        
for j in range(1,l+1):
                print("*",end=" ")
        
