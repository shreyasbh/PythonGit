class Bike(object):
    def __init__(self,name):        
        self.name = name
        
    def ride(self):
        print("riding a bike")
        
    def __str__(self):
        print(str(self.name))