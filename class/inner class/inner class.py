"""class school:
        def __init__(self,name,age,rollno):
                self.name=name
                self.age=age
                self.rollno=rollno
        def grade(self,rank):
                a=rank
                print("students name",self.name)
                print("students age",self.age)
                print("students rollno",self.rollno)
                print("student secured rank",a)
a=school("abhi",23,305)
a.age=35
a.grade("topper")"""

#innerclass

class school:
        def __init__(self,name,age,rollno):
                self.name=name
                self.age=age
                self.rollno=rollno
        def grade(self,rank):
                a=rank
                print("students name",self.name)
                print("students age",self.age)
                print("students rollno",self.rollno)
                print("student secured rank",a)

        class group:
                def __init__(self,leader,colour):
                        self.leader=leader
                        self.colour=colour
                        print("students leader",self.leader)
                        print("students colour",self.colour)
               

o=school("abhi",23,305)
o.grade(1)
s=o.group("yes","red")




                        
                
















        

                
        
                



