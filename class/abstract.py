class Grandfather:
        def land(self):
                pass
class Dad(Grandfather):
        def property(self,number):
                print(number,"is the property gained by dad")
class Son(Grandfather):
        def gained(self,newer):
                print(newer,"it the new number of property gained by son")
e=Son()
e.land()
e.gained("200")

