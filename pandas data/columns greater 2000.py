import pandas as pd
a=pd.read_csv("data/crops.csv")
b=a[a["yield(quintal)"]>100000]
print(b)
