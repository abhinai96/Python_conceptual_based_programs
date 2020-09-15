a=20
def something():
        a=100
        x=globals()['a']
        print("inside function",a)
        globals()['a']=5
something()
print("outside function",a)
