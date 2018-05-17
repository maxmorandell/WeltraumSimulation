'''
Die Nebenklasse für den China-Planeten!
@author: Stefan Plattner, Max Morandell
'''

from planeten import Planeten
from random import randint

class China(Planeten):
     
    def __init__(self):
        super().__init__()
        self.setPreis()
        #Planeten-spezifische Preise festgelegt.
    def setPreis(self):
        self.planetenPreis['vodka'] = randint(35,65)
        self.planetenPreis['mikrocontroller'] = randint(10,25)
        self.planetenPreis['schnitzel'] = randint(12,53)
        
    def getPreis(self):
        return Planeten.getPreis(self)