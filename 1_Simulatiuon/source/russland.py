'''
Die Nebenklasse für den Russland-Planeten!
@author: Stefan Plattner, Max Morandell
'''

from planeten import Planeten
from random import randint

class Russland(Planeten):
     
    def __init__(self):
        super().__init__()
        self.setPreis()
        #Planeten-spezifische Preise festgelegt.
    def setPreis(self):
        self.planetenPreis['schnitzel'] =  randint(20,45)
        self.planetenPreis['mikrocontroller'] = randint(10,25)
        self.planetenPreis['vodka'] = randint(5,12)
    
    def getPreis(self):
        return Planeten.getPreis(self)