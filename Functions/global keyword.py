a=10

def update():
        a=35
        x=globals()['a']
        print("inside function",a)
        
        globals()['a']=50
        
update()
print("outside function",a)




