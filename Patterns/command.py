class Remote(object):
    def __init__(self):
        self.commands = []
    
    def addCommand(self,command):
        self.commands.append(command)

    def runCommands(self):
        for command in self.commands:
            command.execute()
    
    
class Light(object):
    def on(self):   
        print("Switch on the light")
    def off(self):
        print("Switch off the light")
        
class LightOn(object):
    def __init__(self,light):
        self.light = light
    def execute(self):
        self.light.on()
        
class LightOff(object):
    def __init__(self,light):
        self.light = light
    def execute(self):
        self.light.off()
        
remoteControl = Remote()
light = Light()
lightOn = LightOn(light)
lightOff = LightOff(light)
remoteControl.addCommand(lightOn)
remoteControl.addCommand(lightOff)
remoteControl.runCommands()


        