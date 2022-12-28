pokemoni = ['Pikachu', 'Charizard', 'Blastoise', 'Inteleon']
print(pokemoni)
list(pokemoni)

print(list(enumerate(pokemoni)))

pokemoni.append(input('Napis pokemona: '))
print(pokemoni)
print(list(enumerate(pokemoni)))

evoluce = ['Raichu', 'Charmander', 'Squirtel', 'Sqibble']

print(list(zip(pokemoni, evoluce)))


from itertools import zip_longest
print(list(zip_longest(pokemoni, evoluce, fillvalue='Missigno')))


evoluce.append(input('Napis evoluci: '))
from itertools import zip_longest
for pkmn, evo in zip_longest(pokemoni, evoluce):
    if pkmn == None:
        pkmn = 'Ditto'
    if evo == None:
        evo = 'Dittinka'
    print((pkmn, evo))