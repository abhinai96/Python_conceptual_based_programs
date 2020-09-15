print("1=shopping")
print("2=movie")
print("3=cricket")
try:
        n=int(input("enter any number 1/2/3:"))
        if n<3:
                print("you are eligible")

except:
        print("its an ERROR")
finally:
        print("after finishing go to home")

"""a=10
try:
        b=(a/0)
        print(b)
except:
        print("a divisble by zero gives infinity")
finally:
        print("hai")"""
