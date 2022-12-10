#Výpočet pro bod varu toluenu v závislosti na tlaku
from math import e

rozmezi = range((int(input("Jaká je počáteční teplota (C°)?: ")))+273,int(input("Jaká je konečná teplota (C°)?: "))+273)

def Clausius():
    
    T1 = 298
    P1 = 3800
    Hvap = 38000
    T2 = x
    exponent = float(((Hvap)/(8.314))*(1/(T1)-1/(T2)))
    soucinitel = float(e**exponent)
    P2 = int((P1*soucinitel))
    print("T= ", x,"K", " P= ",P2, " Pa")


for _ in rozmezi:
    x = _
    Clausius()

