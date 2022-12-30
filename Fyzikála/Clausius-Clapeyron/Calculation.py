import List_loading
from List_loading import solvent_names, solvent_temperature, solvent_enthalpy
import Choose
from Choose import chosen_solvent
from math import e


Temperature_range = range((int(input("What's the starting temperature (C°)?: ")))+273,int(input("What's the final temperature (C°)?: "))+273)

def Clausius():
    
    T1 = (float(solvent_temperature[chosen_solvent])+273)
    P1 = 100000
    Hvap = int(solvent_enthalpy[chosen_solvent])
    T2 = x
    exponent = float(((Hvap)/(8.314))*(1/(T1)-1/(T2)))
    soucinitel = float(e**exponent)
    P2 = int((P1*soucinitel))
    print("T= ", x,"K", " P= ",P2, " Pa")


for _ in Temperature_range:
    x = _
    Clausius()

