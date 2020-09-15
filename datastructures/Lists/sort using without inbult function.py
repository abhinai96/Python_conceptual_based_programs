lst=[5,2,3,4,1]
for i in range(len(lst)):
        min_val=min(lst[i:])
        min_index=lst.index(min_val)
        lst[i],lst[min_index]=lst[min_index],lst[i]
print(lst)
