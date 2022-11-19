print("DnD kostka more!!!!!")
from random import randrange
kostky = range(int(input("Pocet kostek, gadzo: ")))
def hod_kostkou():
    for x in kostky:
        kostka = randrange(1,13)
        if kostka <= 3:
            print(kostka, "O kurwa....")
        if kostka > 3 and kostka<=6 :
            print(kostka, "Do pierdole!")
        if kostka > 6 and kostka<=9 :
            print(kostka, "Se da!")
        if kostka > 9 and kostka<=11:
            print(kostka, "Jedem vole!!!!")
        if kostka == 12:
            print(kostka, "CRITZKRIEG!!!!!")
hod_kostkou()
