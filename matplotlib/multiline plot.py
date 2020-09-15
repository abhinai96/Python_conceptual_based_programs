import matplotlib.pyplot as plt
import pandas as pd
a=pd.DataFrame({"years":[2017,2018,2019,2020],
                "abhisales":[2000,3000,4000,5000],
                "madhusales":[5000,2000,1000,500]})
ax=a.plot(x="years",y="abhisales",kind="line",label="abhi sales ",style="r-.")
a.plot(x="years",y="madhusales",kind="line",ax=ax,label="madhu sales",title="never give up abhi")
ax.set(xlabel="years",ylabel="sales",xticks=a["years"])
plt.show()

