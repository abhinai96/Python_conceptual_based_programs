class student:
        college="st peters"
        def __init__(self,name,roll):
                self.name=name
                self.roll=roll
        def display(self):
                print("students name",self.name)
                print("students rollno",self.roll)
                print("college name is",student.college)
s=student("abhi",305)
s.display()
