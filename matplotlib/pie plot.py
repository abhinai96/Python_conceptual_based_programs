import matplotlib.pyplot as plt
names=["abhi","madhu","shiva","sachin"]
ages=[100,30,50,40]
colors=["r","g","k","b"]
explode=(0,0,0,0)
plt.pie(ages,labels=names,colors=colors,startangle=50,shadow=True,explode=explode)
plt.title("names and ages")
plt.show()
