from adapterlib import Bike 

class Car(object): 
    def __init__(self,name):
        self.name = name
        
    def drive(self):
        print("Driving a car")
        
    def __str__(self):
        print(str(self.name))


class Adapter(object): 
    def __init__(self,obj,methods):
        self.obj = obj 
        self.__dict__.update(methods)
        
        
def main():
    car = Car("Car")
    bike = Bike("Bike")
    adaptedBike = Adapter(bike,dict(drive=bike.ride))
    adaptedBike.drive()
    car.drive()
    
        
if __name__ == "__main__":
    main()
    
        
