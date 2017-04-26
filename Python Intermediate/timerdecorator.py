def timer(originalFunc):
    import time
    
    def wrapper(*args,**kwargs):
        t1 = time.time()
        res = originalFunc(*args,**kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(originalFunc.__name__,t2))
        return res
    return wrapper

@timer    
def display(name,age):
    print('display ran with arguements {} and {}'.format(name,age))
    
display("Tom", 20)

display("Tim", 25)
    