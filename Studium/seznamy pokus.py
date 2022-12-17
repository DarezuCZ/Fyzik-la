from random import randrange
pocet_vrhu = range(int(input('Kolik kostek vrháš?: ')))

dosud = []

for _ in pocet_vrhu:
    vrhy = randrange(1,13)
    print(vrhy)
    dosud.append(vrhy)

dosud.sort()
dosud.reverse()
print(dosud)
