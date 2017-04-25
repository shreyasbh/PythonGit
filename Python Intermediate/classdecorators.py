class decoratorClass(object):
    def __init__(self,originalFunc):
        self.f = originalFunc
        
    def __call__(self,*args,**kwargs):
        print("Class decorated the function")
        return self.f(*args,**kwargs)

@decoratorClass
def display():
    print("Display")
    
display()