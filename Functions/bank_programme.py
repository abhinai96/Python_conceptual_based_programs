def bank():
        print("************************************BANK********************************"   )
        print("enter ,1, for deposit")
        print("enter ,2, for withdraw")

        c=int(input("enter any key for banking 1/2:"))

        if c==1:
                print("************************deposit**************************************")
                print("enter how much you want to deposit")
                n=int(input("enter deposit amount"))
                if n>20000:
                        print("you have exceeded the limit")
                else:
                        print(n,"you have deposited ")
                        print("*****************Thank you visit us again********************")
        if c==2:
                print("withdraw")
                print("how much you want to withdraw")
                m=int(input("enter withdraw amount"))
                if m>10000:
                        print("you have exceeded the limit")
                else:
                        print(m,"you have withdrawn")
                        print("*****************Thank you visit us again**********************")
bank()
