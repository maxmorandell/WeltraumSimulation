'''
Die Nebenklasse für den Frachter!
@author: Stefan Plattner, Max Morandell
'''
from raumschiff import Raumschiff
from random import randint

class Frachter(Raumschiff):

    #Frachterladung zufällig in einem Bereich generieren lassen.
    #Preis setzt sich aus dem Leben und der Laderaumgroesse zusammen.
    def __init__(self):
        super().__init__()
        self.frachterLadung = randint(50,100)
        self.frachterPreis = self.raumschiffLeben * self.frachterLadung 
      
    def getfrachterLadung(self):
        return self.frachterLadung
      
    def getfrachterPreis(self):
        return self.frachterPreis
