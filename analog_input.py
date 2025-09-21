

class AnalogInput:
    def __init__(self, name, euMin, euMax, rawMin, rawMax, raw):
        self.name = name
        self.euMin = euMin
        self.euMax = euMax
        self.rawMin = rawMin
        self.rawMax = rawMax
        self.raw = raw

    def scaling(self):
        scaled = self.euMin + ((self.euMax-self.euMin)*(self.raw-self.rawMin)/ (self.rawMax-self.rawMin))
        return scaled
        

    def __str__(self):
        return f"{self.name}"
    


sensor = AnalogInput("TIT", 0, 10, 4, 20, 12)

print(sensor.scaling())
print(sensor.name)

