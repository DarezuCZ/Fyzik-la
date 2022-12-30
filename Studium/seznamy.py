pokemoni = ['Zoroark', 'Inteleon', 'Decidueye']
print(pokemoni)
pokemoni.append('Darkai')
print(pokemoni)

for pokemon in pokemoni:
    print(pokemon.upper())

print(len(pokemoni))

abeceda = list('abcdefghijklmnopqrstuvwxyz')
cisla = list(range(100))
print(abeceda)
print(cisla)

slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(slova)

zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy)

veta = ' '.join(slova)
print(veta)

import random

ciselne_hodnoty = list(range(2, 11))
pismenne_hodnoty = list('JQKA')

balicek = []
for barva in '♠', '♥', '♦', '♣':
    for hodnota in ciselne_hodnoty + pismenne_hodnoty:
        balicek.append(str(hodnota) + barva)
print(balicek)

random.shuffle(balicek)
print(balicek)