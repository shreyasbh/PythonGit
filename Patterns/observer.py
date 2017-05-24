from abc import ABCMeta, abstractmethod

class Publisher(object):
    
    def __init__(self):
        self.observers = []
        
    def addObserver(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            raise Error("Already in observer")

    def removeObserver(self,observer):
        self.observers.remove(observer)
        
    def publishUpdate(self):
        for observer in self.observers:
            message = "32.0" + " 100"  
            observer.update(message)
            
class Observer(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self,message):
        pass
        
class displayFirst(Observer):
    def update(self,message):
        first = message.split(" ")[0]
        print(first)
        
class displaySecond(Observer):
    def update(self,message):
        second = message.split(" ")[1]
        print(second)
        
if __name__ == "__main__":
    
    pub = Publisher() 
    df = displayFirst()
    ds = displaySecond()
    pub.addObserver(df)
    pub.addObserver(ds)
    pub.publishUpdate()
    
        