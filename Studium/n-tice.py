osoby = 'máma', 'teta', 'babička'
for osoba in osoby:
    print(osoba)

prvni = osoby[0]
print(f'První je {prvni}')


seznam_dvojic = []
for i in range(10):
    # `append` bere jen jeden argument; dáme mu jednu dvojici
    seznam_dvojic.append((i, i**2))
print(seznam_dvojic)

ix, ocko = 'xo'
jedna, dva, tri = [1, 2, 3]
print(jedna)

kamen, nuzky, papir = [1, 2, 3]
print(papir)