def noLogging():
    print("Do stuff")

def logBefore():
    print("Logging before doing stuff")
    print("Do Stuff")

def logAfter():
    print("Do stuff")
    print("Logging after doing stuff")
    
def template(default=noLogging):
    print("---------")
    default()
    print("---------")



    
template()
template(logBefore)
template(logAfter)
