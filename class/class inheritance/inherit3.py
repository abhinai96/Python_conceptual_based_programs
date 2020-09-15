
class Automobiles:
        def requirements(self,breaks,engineoil):
                print(breaks,"for car")
                print(engineoil,"for car")
class Marutisuzki(Automobiles):
        def alto(self,seating,petrol):
                print(seating,"for alto")
                print(petrol,"for alto")
class Hyundai(Marutisuzki):
        def i10(self,cc,autogears):
                print(cc,"the speed")
                print(autogears,"for i10")
a=Hyundai()
a.requirements("vaccum","castrol")
a.alto(5,"12lit")
a.i10(1000,"yes")
