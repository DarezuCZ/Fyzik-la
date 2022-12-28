def vytvor_radek_tabulky(cislo_radku, velikost):
    """Vrátí seznam – daný řádek tabulky s násobilkou"""
    radek = []
    for cislo_sloupce in range(velikost):
        radek.append(cislo_radku * cislo_sloupce)
    return radek

def vytvor_tabulku(velikost):
    """Vrátí seznam seznamů – tabulku s násobilkou"""
    seznam_radku = []
    for cislo_radku in range(velikost):
        radek = vytvor_radek_tabulky(cislo_radku, velikost)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku(11)

print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()