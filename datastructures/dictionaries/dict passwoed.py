password=int(input("enter passwd"))
realpassword=(12345)
dictionary = {'Age':"27",'edu':'B.tech','city':'hyd'}
if password==realpassword:
        print("password is ok")
        print("dict values Age ,edu,city")
        for i in dictionary.keys():
                a=input("enter dict value")
                if a==i:
                        print(dictionary.get(i))
else:
        print("enter correct passwd")

        



