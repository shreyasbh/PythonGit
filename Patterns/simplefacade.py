class WatchTVFacade(object): 
    
    def __init__(self):
        self.tv = TV()
        self.sound = SurroundSound()
        self.light = Light()
      
    def watchNow(self):
        self.light.turnOn()
        self.light.dimLight()
        self.tv.turnOn()
        self.sound.turnOn()
        self.sound.changeVolume()
        
                
class TV(object):
    
    def turnOn(self):
        print("Turn TV On")
    
    def turnOff(self):
        print("Turn TV off")
        
class SurroundSound(object):
    
    def turnOn(self):
        print("Turning on surround sound")
    
    def turnOff(self):
        print("Turning off surround sound")
        
    def changeVolume(self):
        print("Changing the volume")
        
class Light(object):
    
    def turnOn(self):
        print("Turning on light")
        
    def turnOff(self):
        print("Turing off light")
        
    def dimLight(self):
        print("Dimming light")
        
if __name__ == "__main__":
    watchTV = WatchTVFacade()
    watchTV.watchNow()
        
    