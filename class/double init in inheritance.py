class a:
        def __init__(self):
                print("in a is init")
        def feature1(self):
                print("feature1 is working")
        def feature2(self):
                print("feature2 is working")
class b(a):
        def __init__(self):
                super().__init__()
                print("in b is init")
        def feature3(self):
                print("feature 3 is working")
o=b()
o.feature1()
o.feature2()
o.feature3()
