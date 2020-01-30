class Country:
    ID_TAG = 'N/A'
    GDP = 0
    ARMY_ASSETS = 0
    NAVY_ASSETS = 0
    AIR_FORCE_ASSETS = 0
    MANPOWER = 0
    NUCLEAR_CAPABILITIES = 0

    def __init__(self,a='N/A',b=0,c=0,d=0,e=0,f=0,g=0):
        ID_TAG = a
        GDP = b
        ARMY_ASSETS = c
        NAVY_ASSETS = d
        AIR_FORCE_ASSETS = e
        MANPOWER = f
        NUCLEAR_CAPABILITIES = g

    def toString(self):
        print(self.ID_TAG)
        print(self.GDP)
        print(self.ARMY_ASSETS)
        print(self.NAVY_ASSETS)
        print(self.AIR_FORCE_ASSETS)
        print(self.MANPOWER)
        print(self.NUCLEAR_CAPABILITIES)

