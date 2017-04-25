def decoratedPrint(inpFunc):
    def wrapperPrint(*args,**kwargs):
        print("Decorating before")
        return inpFunc(*args,**kwargs)
    return wrapperPrint

def inpFunc():
    print("wrapped function 1")
    

dec_inpFunc = decoratedPrint(inpFunc)
dec_inpFunc()

@decoratedPrint
def inpFunc2():
    print("wrapped function 2")
    
inpFunc2()

@decoratedPrint
def func3(name,age):
    print(name+age)
    
func3("Shreyas","Bhag")