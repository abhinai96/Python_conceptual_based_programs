import pandas as pd
weather=[('1/1/2020',30,'rainy'),('1/6/2020',40,'sunny'),('1/12/2020',25,'snow')]
a=pd.DataFrame(weather,columns=["date","temp","weather"])
print(a)
