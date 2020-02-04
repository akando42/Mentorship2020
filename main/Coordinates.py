import numpy as np

class Cords:
    lat = 0.0
    long = 0.0

    def __init__(self,lat = 0.0, long = 0.0):
        self.lat = lat
        self.long = long

    def get_loc(self):
        return self.lat, self.long

    def set_loc(self,x,y):
        self.lat = x
        self.long = y

    def set_rand_cords(self):
        self.lat = np.random.uniform(-180,180)
        self.long = np.random.uniform(-90,90)


r = Cords(2.0,2.0)
r.set_rand_cords()
print(r.get_loc())

