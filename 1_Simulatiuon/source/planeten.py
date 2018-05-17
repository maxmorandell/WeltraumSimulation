'''
Die Hauptklasse für die Planeten!
@author: Stefan Plattner, Max Morandell
'''
from random import randint


class Planeten:
    
    #Definieren, dass es für die 3 Produkte einen Preis gibt.
    #Zufällige Planeten-Nummer generieren
    #Planetname setzt sich aus Planet und der zufällig generierten Zahl
    #zusammen.
    
    def __init__(self):
        super().__init__()
        preis = {'schnitzel': 0, 'mikrocontroller': 0, 'vodka':0}
        self.planetenPreis = preis
        self.planetenNummer = randint(10,100)*3
        self.planetenName = "Planet" + str(self.planetenNummer)
    
    def getPreis(self):
        return self.planetenPreis
    
    def getPlanetName(self):
        return self.planetenName
    