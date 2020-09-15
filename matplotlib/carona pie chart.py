import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_excel("carona.xlsx")

colors=["r","k","g","b","y"]
explode=(0,0,0,0,0)
plt.pie(a["carona"],labels=a["country"],colors=colors,startangle=50,shadow=True,explode=explode,autopct="%1.1f%%")
plt.title("carona pie plot")
plt.show()
fig=plt.figure()
plt.savefig("samplepie",bbox_inches="tight")
