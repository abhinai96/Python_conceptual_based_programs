shp_lst=["milk","bread","eggs"]
prices={"milk":23,"bread":40,"eggs":5}
stock={"milk":100,"bread":200,"eggs":50}
total=0
cart=[]
for i in shp_lst:
        item=i
        bill=prices[i]
        print(i,"enter the items")
        quantity=int(input("enter the qunatity"))
        print(i,":",bill,"*",quantity,"=",bill*quantity)
        total=total+bill*quantity
        total1=i,"=",bill*quantity
        cart.append(total1)
        stock[i]=stock[i]-quantity
print("cart=",cart)
print()
print("the total bill is ", total)
print()
customer_pay=int(input("enter payment=="))
if customer_pay<total:
        print("you need to pay more",total-customer_pay)
elif customer_pay>total:
        print("customer change",total-customer_pay)
else:
        print("thank you,visit us again")
print(" stock available is =",stock)

        
