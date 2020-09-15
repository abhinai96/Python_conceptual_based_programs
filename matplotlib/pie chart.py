import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_excel("train data.xlsx")
b=print(a.head())
colors=["r","g","b","k","y"]
explode=(0,0,0,0,0)
plt.pie(a["dep"],labels=a["duration"],colors=colors,startangle=50,explode=explode,shadow=True,autopct="%1.1f%%")
plt.size("data pie chart")
plt.show()
