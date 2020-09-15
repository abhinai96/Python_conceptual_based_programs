class Kphb:
        def __init__(self,Institutename,area):
                self.i=Institutename
                self.a=area
        def datascience(self,coursefees,days,coursename):
                c=coursefees
                d=days
                x=coursename
                print("institute name",self.i)
                print("area",self.a)
                print("coursename",x)
                print("course fees",c)
                print("days",d)
        def blockchain(self,coursefees,days,coursename):
                e=coursefees
                f=days
                y=coursename
                print("institute name",self.i)
                print("area",self.a)
                print("coursename",y)
                print("course fees",e)
                print("days",f)
print("1=datascience")
print("2=blockchain")
g=Kphb("aditi","kphb")
k=int(input("enter number to decide which course 1/2"))
if k==1:
        g.datascience(40000,90,"datascience")
if k==2:
        g.blockchain(20000,20,"blockchain")
            
        
                
        
                
        
