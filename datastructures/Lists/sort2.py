lst=[3,5,2,1,4]
lst1=[]


while lst:
        min=lst[0]
        for i in lst:
                if i<min:
                        min=i
        lst1.append(min)
        lst.remove(min)
        
print(lst1)
