"""lst=[5,6,2,3,1,4]
lst1=[]


while lst:
        min=lst[0]
        for i in lst: 
                if i<min:
                        min=i
        lst1.append(min)
        lst.remove(min)
                        
        
print(lst1)"""

lst=[5,6,2,3,1,4]
lst1=[]

min=lst[0]
n=len(lst)

for i in range(1,n):
        if lst[i]<min:
                min=lst[i]
lst1.append(min)
lst.remove(min)

print(lst1)
        
        
                
        
        
        
