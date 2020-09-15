def casino():
       while True:
              print("calculator programme")
              print("0=addition") 
              print("1=subtraction")
              print("2=multiplication")
              print("3=division")
              print("4=double division")
              print("5=remainder")



              j=input("enter the operations number required here 0/1/2/3/4/5")


              i=int(input("enter the number1"))

              k=int(input("enter the number2"))

              if j=="0":
                     print(i+k,"added")
              elif j=="1":
                     print(i-k,"subtracted")
              elif j=="2":
                     print(i*k,"mutliplied")
              elif j=="3":
                     print(i/k,"divided")
              elif j=="4":
                     print(i//k,"prior decimal numbers")
              elif j=="5":
                     print(i%k,"remainder")
              else:
                     print("you have not selected correct operater")
casino()
