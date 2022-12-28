

cisla_prvni = range(11)
cisla_druha = range(11)
cisla_treti = range(11)
radek = []
sloupec = []
tabulka = []
for x in cisla_prvni:
    radek.append(x)
    for y in cisla_druha:
        sloupec.append(y)
        tabulka.append((x*y))

for z in cisla_treti:
    print(tabulka[(z*11):(11*(1+z))])

