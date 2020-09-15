import matplotlib.pyplot as plt
import pandas as pd
labels=["delhi","mumbai","banglore","kerala"]
x1=[45,60,55,10]
x2=[65,41,62,14]

a=pd.DataFrame({"2017score":x1,
                "2018score":x2,
                "cities":labels})
fig=plt.figure()

ax1=fig.add_subplot(121)
ax=a.plot(x="cities",y="2017score",kind="bar",ax=ax1,title="2017score")
ax2=fig.add_subplot(122)
ax=a.plot(x="cities",y="2018score",kind="bar",ax=ax2,title="2018score")
plt.show()
plt.savefig("hist1.pdf",bbox_inches="tight",pad_inches=2)

