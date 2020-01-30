import numpy as np

class Coords:
    lat = 0.0
    long = 0.0

    def __init__(self,lat = 0.0, long = 0.0):
        self.lat = lat
        self.long = long

    def getLoc(self):
        return self.lat, self.long

    def setLoc(self,x,y):
        self.lat = x
        self.long = y

    def setRandCoords(self):
        self.lat = np.random.uniform(-180,180)
        self.long = np.random.uniform(-90,90)

r = Coords(2.0,2.0)
print(r.getLoc())

