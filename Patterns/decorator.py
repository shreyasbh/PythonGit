def printDecorator(func):
    def printWrapper():
        print("Print from the decorator")
        return func()
    return printWrapper
    
 
@printDecorator 
def doSomething():
    print("Print from doSomething")
    
def doNothing():
    print("Print from doNothing")

doNothing = printDecorator(doNothing)

doSomething()
doNothing()

