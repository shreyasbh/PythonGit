#python functions are first class objects.

def OnePlus(x):
    return x + 1
    
def Mul10(x):
    return x * 10    

def my_map(func, x):
    return func(x)
    

print(my_map(OnePlus,10))
print(my_map(Mul10,10))
