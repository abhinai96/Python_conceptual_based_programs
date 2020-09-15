a=float(input("enter one side"))
b=float(input("enter second side"))
c=float(input("enter  third side"))
s=(a+b+c)/2      #formula for perimeter
print(s,"perimeter of traingle")

area=(s*(s-a)*(s-b)*(s-c))**2   #formula of the traingle
print(area,"area of traingle")
