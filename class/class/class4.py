print("1=square star")
print("2=triangle star")
class Loops:
        def square():
                a=5
                for i in range(1,a+1):
                        for j in range(1,a+1):
                                print("*",end=" ")
                        print()

        def triangle():
                a=5
                for i in range(1,a+1):
                        for j in range(1,i+1):
                                print("*",end=" ")
                        print()
o=Loops
j=int(input("which pattern you need 1/2:"))
if j==1:
        print(o.square())
if j==2:
        print(o.triangle())
