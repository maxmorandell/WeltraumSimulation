'''
Die Nebenklasse für den Jaeger!
@author: Stefan Plattner, Max Morandell
'''
from raumschiff import Raumschiff
from random import randint

class Jaeger(Raumschiff):
    
    #Schusskraft des Jaegers zufällig generieren lassen.
    #Preis des Jaegers setzt sich aus der Schusskraft und dem Leben zusammen.
    def __init__(self):
        super().__init__()
        self.jaegerSchusskraft = randint(20, 150)
        self.jaegerPreis = self.jaegerSchusskraft * self.raumschiffLeben
        
    def getjaegerSchusskraft(self):
        return self.jaegerSchusskraft 
        
    def getjaegerPreis(self):
        return self.jaegerPreis