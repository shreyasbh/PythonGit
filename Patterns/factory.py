#Simple example for a factory pattern 

class CarSedan(object):
    def driveCar(self):
        print("Driving Sedan")
        
class CarSUV(object):
    def driveCar(self):
        print("Driving SUV")
        
def carFactory(name):
    if name == "Sedan":
        car = CarSedan()
    elif name == "SUV":
        car = CarSUV()
    else:
        raise ValueError("Connot find car type {}".name)
    return car
    
def carConnect(name):
    factory = None
    try:
        factory = carFactory(name)
    except ValueError as ve:
        print(ve)
    return factory
    
car1 = carConnect("SUV")
car1.driveCar()