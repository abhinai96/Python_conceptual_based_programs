"""import pandas as pd
a={"0":[20,24,27],"1":["aj",25,"abhi"],"2":[23,"raj",30]}
data=pd.DataFrame(a)
print(data)"""

import pandas as pd
a={"names":["abhi","raj","nagbabu"],"heights":[510,59,511],"weights":[55,65,85]}
data=pd.DataFrame(a)
print(data[["heights"]])


