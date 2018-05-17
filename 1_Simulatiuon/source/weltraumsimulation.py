'''
Die Game-Klasse in der der komplette Spielablauf ist!
@author: Stefan Plattner, Max Morandell
'''

#Klassen und Funktionen werden importiert.
from frachter import Frachter
from jaeger import Jaeger
from austria import Austria
from china import China
from russland import Russland
from random import randint
import sys

#Erstellung der Hauptvariablen
Geld = 25000
Schiffe = {'jaeger' : 0, 'frachter' : 0}
Waren = {'schnitzel' : 0, 'mikrocontroller' : 0, 'vodka' : 0}
derzeitigerPlanet = None


#Erstellen und Auswahl der Planeten
def planetErstellen():
    
    global derzeitigerPlanet
    
    while(True):
        print("Wählen Sie bitte einen Planeten: \n")
        print("Zur Auswahl stehen Planeten mit den Themen Oesterreich, China & Russland:")
        print("Für Oesterreich druecken Sie bitte die [1]")
        print("Für China druecken Sie bitte die [2]")
        print("Für Russland druecken Sie bitte die [3]")
        print("________________________________________________")
        ihreWahl = input()
        
        if(ihreWahl == "1"):
            derzeitigerPlanet = Austria()
            print("Sie haben das Thema Oesterreich gewaehlt:")
            print("________________________________________________")
            break
        if(ihreWahl == "2"):
            derzeitigerPlanet = China()
            print("Sie haben das Thema China gewählt")
            print("________________________________________________")
            break
        if(ihreWahl == "3"):
            derzeitigerPlanet = Russland()
            print("Sie haben das Thema Russland gewählt")
            print("________________________________________________")
            break
        print("Bitte geben Sie eine Zahl zwischen 1 & 3 ein!")
        print("________________________________________________")
        
 
#Funktion um Raumschiffe zu kaufen      
def raumschiffKaufen():
    
    global Geld
    global Schiffe
    Kampfschiff = Jaeger()
    JaegerPreis = Kampfschiff.getjaegerPreis()
    Transportschiff = Frachter()
    FrachterPreis = Transportschiff.getfrachterPreis()
        
    print("Wählen Sie bitte ein Schiff das Sie kaufen moechten:")
    print("Zur Auswahl stehen ein Jaegerschiff und ein Frachtschiff \n")
    print("Diese Schiffe besitzen Sie [0]")
    print("Für das Jaegerschiff druecken Sie bitte die [1]")
    print("Für das Frachtschiff druecken Sie bitte die [2]")
    print("Preis Jaeger:" + str(JaegerPreis) + ", Preis Frachter:"+ str(FrachterPreis))
    print("Aktuelles Guthaben:" + str(Geld))
    print("________________________________________________")
    
    ihreWahl = input()
    
    if(ihreWahl == "0"):
        print("Diese Schiffe besitzen Sie! \n") 
        print(Schiffe)
        print("________________________________________________")
            
        
    elif(ihreWahl == "1"):
        if(Geld >= JaegerPreis):
            Geld = Geld - JaegerPreis
            Schiffe['jaeger'] += 1
            print("Sie haben ein Jaegerschiff gekauft \n")
            print("________________________________________________")
            
        else:
            print("Ihr Guthaben ist zu klein \n")
            print("________________________________________________")
            
                
    elif(ihreWahl == "2"):
        if(Geld >= FrachterPreis):
            Geld = Geld - FrachterPreis
            Schiffe['frachter'] += 1 
            print("Sie haben ein Frachtschiff gekauft \n") 
            print("________________________________________________")
            
        else: 
            print("Ihr Guthaben ist zu klein \n")
            print("________________________________________________")
            
    else:         
        print("Bitte geben Sie eine Zahl zwischen 0 & 2 ein! \n")
        print("________________________________________________")
    
#Funktion um Waren zu kaufen 
def warenKaufen():
    
    global derzeitigerPlanet
    global Waren
    global Geld
    Preise = derzeitigerPlanet.getPreis()
    Lager = Frachter()
    Platz = Lager.getfrachterLadung()
    
    print("Wählen Sie bitte eine Ware um diese zu erwerben:")
    print("Zur Auswahl stehen Schnitzel, Mikrokontroller & Vokda \n")
    print("Diese Waren besitzen Sie [0]")
    print("Um ein Schnitzel zu kaufen druecken Sie bitte die [1]")
    print("Um einen Microchip zu kaufen druecken Sie bitte die [2]")
    print("Um Vodka zu kaufen druecken Sie bitte die [3]")
    print("Aktuelle Waren Preise :" + str(Preise))
    print("Aktuelles Guthaben:" + str(Geld))
    print("________________________________________________")
    
    ihreWahl = input()
    
    if(ihreWahl == "0"):
        print("Diese Waren besitzen Sie! \n") 
        print(Waren)
        print("________________________________________________")
            
            
    elif(ihreWahl == "1"):
        print("Nun bitte Anzahl der Ware angeben: \n")
        anzahl = input()
        if(Geld >= Preise['schnitzel'] * int(anzahl) and Platz >= int(anzahl)):
            Geld = Geld - Preise['schnitzel'] * int(anzahl)
            Waren['schnitzel'] += 1 * int(anzahl)
            print("Sie haben " + str(anzahl) + " Schnitzel gekauft")
            print("________________________________________________")
            
        else:
            print("Ihr Guthaben/Ladefläche ist zu klein")
            print("________________________________________________")
                
    elif(ihreWahl == "2"):
        print("Nun bitte Anzahl der Ware angeben: \n")
        anzahl = input()
        if(Geld >= Preise['mikrocontroller'] * int(anzahl) and Platz >= int(anzahl)):
            Geld = Geld - Preise['mikrocontroller'] * int(anzahl)
            Waren['mikrocontroller'] += 1 * int(anzahl)
            print("Sie haben " + str(anzahl) + " Mikrocontroller gekauft") 
            print("________________________________________________")
            
        else:
            print("Ihr Guthaben/Ladefläche ist zu klein")
            print("________________________________________________")

        
    elif(ihreWahl == "3"):
        print("Nun bitte Anzahl der Ware angeben: \n")
        anzahl = input()
        if(Geld >= Preise['vodka'] * int(anzahl) and Platz >= int(anzahl)):
            Geld = Geld - Preise['vodka']* int(anzahl)
            Waren['vodka'] += 1 * int(anzahl)
            print("Sie haben " + str(anzahl) + " Vodka gekauft")
            print("________________________________________________")
            
        else:
            print("Ihr Guthaben/Ladefläche ist zu klein")
            print("________________________________________________")
            
    else:         
        print("Bitte geben Sie eine Zahl zwischen 0 & 3 ein!")
        print("________________________________________________")
    

#Funktion um Waren zu verkaufen
def warenVerkaufen():
    
    global derzeitigerPlanet
    global Waren
    global Geld
    Preise = derzeitigerPlanet.getPreis()
    
    print("Wählen Sie bitte eine Ware um diese zu verkaufen:")
    print("Zur Auswahl stehen Schnitzel, Mikrokontroller & Vokda")
    print("Diese Waren besitzen Sie [0]")
    print("Um ein Schnitzel zu verkaufen druecken Sie bitte die [1]")
    print("Um einen Microchip zu verkaufen druecken Sie bitte die [2]")
    print("Um Vodka zu verkaufen druecken Sie bitte die [3]")
    print("Aktuelle Waren Preise :" + str(Preise))
    print("Aktuelles Guthaben:" + str(Geld))
    print("________________________________________________")
    ihreWahl = input()
       
    if(ihreWahl == "0"):
        print("Diese Waren besitzen Sie!") 
        print(Waren)
        print("________________________________________________")
            
            
    elif(ihreWahl == "1"):
        print("Nun bitte Anzahl der Ware angeben:")
        anzahl = input()
        if(Waren['schnitzel'] >= int(anzahl)):
            Geld = Geld + Preise['schnitzel'] * int(anzahl)
            Waren['schnitzel'] -= 1 * int(anzahl)
            print("Sie haben " + str(anzahl) + " Schnitzel verkauft")
            print("________________________________________________")
            
        else: 
            print("Sie können nicht mehr Schnitzel verkaufen als Sie besitzen")
            print("________________________________________________")
            
                
    elif(ihreWahl == "2"):
        print("Nun bitte Anzahl der Ware angeben:")
        anzahl = input()
        if(Waren['mikrocontroller'] >= int(anzahl)):
            Geld = Geld + Preise['mikrocontroller'] * int(anzahl)
            Waren['mikrocontroller'] -= 1 * int(anzahl)
            print("Sie haben " + str(anzahl) + " Mikrocontroller verkauft") 
            print("________________________________________________")
            
        else:
            print("Sie können nicht mehr Mikrocontroller verkaufen als Sie besitzen")
            print("________________________________________________")
        
        
    elif(ihreWahl == "3"):
        print("Nun bitte Anzahl der Ware angeben:")
        anzahl = input()
        if(Waren['mikrocontroller'] >= int(anzahl)):
            Geld = Geld + Preise['vodka']* int(anzahl)
            Waren['vodka'] -= 1 * int(anzahl)
            print("Sie haben"+ str(anzahl) + " Vodka verkauft")
            print("________________________________________________")
            
        else:
            print("Sie können nicht mehr Vodka verkaufen als Sie besitzen")
            print("________________________________________________")
            
            
    else:         
        print("Bitte geben Sie eine Zahl zwischen 0 & 3 ein!")
        print("________________________________________________")
  
#Funktion um den Lagerstand zu erfahren   
def warenStand():
    
    global Waren
    
    print("Diese Waren besitzen Sie!") 
    print(Waren)
    print("________________________________________________")

#Funktion um den Kontostand zu erfahren
def kontostand():
    
    global Geld
    
    print("Das ist Ihr aktueller Kontostand:")
    print(Geld)
    print("________________________________________________")

#Funktion um zu erfahren welche Raumschiffe man besitzt
def raumschiffe():
    
    global Schiffe
    
    print("Diese Schiffe besitzen Sie!") 
    print(Schiffe)
    print("________________________________________________")

#Funktion für den Piraten Angriff
def piratenAngriff():
    
    global Geld
    Schusskraft = Jaeger()
    deinJaeger = Schusskraft.getjaegerSchusskraft()
    schussKraftdeinesGegners = randint(20, 150)
    beute = randint(1,50000)
    
    print("Hilfe Sie werden Angegriffen")
    
    if(deinJaeger == schussKraftdeinesGegners):
        print("Noch mal gut gegangen")
        print("________________________________________________")
    
    elif(deinJaeger <= schussKraftdeinesGegners):
        print("Wir haben den Kampf verloren")
        print("Verdammt!!!")
        if(Geld >= beute):
            Geld = Geld - beute
            print("Aktueller Kontostand nach dem Angriff:" + str(Geld))
            print("________________________________________________")
        
        else: 
            print("Sie haben Verloren")
            print("Gameover")
            sys.exit(0)
        
    elif(deinJaeger >= schussKraftdeinesGegners):
        print("Wir haben gewonnen!!!")
        print("Glück gehabt!!!")
        Geld = Geld + beute
        print("Aktueller Kontostand nach dem Angriff:" + str(Geld))
        print("________________________________________________")

  
#Funktion um weiter zu Reisen      
def reisen():
    
    global Geld
    
    piratenAngriff()
    Geld = Geld - 100
    planetErstellen()


#Spielmenue
def menu():
    
    global derzeitigerPlanet
    ihreWahl = 0
    

    while(True): 
        print("Sie befinden sich am " + derzeitigerPlanet.getPlanetName() + " mit dem Thema " + derzeitigerPlanet.__class__.__name__ + "\n")
        print("Was moechten Sie nun tun?")
        print("Zur Auswahlt steht: \n")
        print("Ein Raumschiff zu kaufen [1]")
        print("Waren kaufen [2]")
        print("Waren verkaufen [3]")
        print("Ihr Lager zu überprüfen [4]")
        print("Ihren Kontostand zu überprüfen [5]")
        print("Ihre Raumschiffe [6]")
        print("Weiter reisen [7]")
        
        ihreWahl = input()
        if(ihreWahl == "1"):
            raumschiffKaufen()
        if(ihreWahl == "2"):
            warenKaufen()
        if(ihreWahl == "3"):
            warenVerkaufen()
        if(ihreWahl == "4"):
            warenStand()
        if(ihreWahl == "5"):
            kontostand()
        if(ihreWahl == "6"):
            raumschiffe()
        if(ihreWahl == "7"):
            reisen()
            
         
#main        
print("#### Willkommen zu unserem Weltraumsimulator ####")
planetErstellen()  
menu()
        
