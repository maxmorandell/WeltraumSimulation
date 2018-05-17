'''
Die Nebenklasse für den Austria-Planeten!
@author: Stefan Plattner, Max Morandell
'''

from planeten import Planeten
from random import randint

class Austria(Planeten):
     
    def __init__(self):
        super().__init__()
        self.setPreis()
    #Planeten-spezifische Preise festgelegt.
    def setPreis(self):
        self.planetenPreis['schnitzel'] =  randint(10,25)
        self.planetenPreis['mikrocontroller'] = randint(50,75)
        self.planetenPreis['vodka'] = randint(7,35)
        
    def getPreis(self):
        return Planeten.getPreis(self)