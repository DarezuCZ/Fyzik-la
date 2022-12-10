from math import log
def Clausius_Clapeyron():
    
    T1 = float(input("Zadej teplotu v kelvinech při které znáš tlak par nad kapalinou: "))
    P1 = float(input("Zadej tlak v pascalech při uvedené teplotě: "))
    Hvap = float(input("Zadej výparné teplo v joulech: "))
    P2 = float(input("Zadej vnější tlak v pascalech: "))
    T2 = ((-1)/((-1/T1)+((8.314/Hvap)*log(P2/P1))))
    print("Bod varu = ", T2, " K")

Clausius_Clapeyron()
