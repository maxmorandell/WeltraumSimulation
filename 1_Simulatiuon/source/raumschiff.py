'''
Die Hauptklasse für die Raumschiffe!
@author: Stefan Plattner, Max Morandell
'''
from random import randint

class Raumschiff():

    #Definieren, dass das Raumschiffleben in einem bestimmten Bereich
    #generiert wird.
    def __init__(self):
        self.raumschiffLeben = randint(1, 100)
      
    def getleben(self):
        return self.raumschiffLeben