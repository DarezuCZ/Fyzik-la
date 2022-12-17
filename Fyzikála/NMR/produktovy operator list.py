import numpy as np

#Konstanty operátorů jsou počítané zvlášť
konstanta_pul_x_z = np.array ([0.5+0j])
konstanta_pul_x_z.imag
array = ([0])
konstanta_y = np.array([0+0.5j])
konstanta_y.imag
array = ([0.5])

#Jednotlivé operátory
u = np.array([[1,0],
                       [0,1]])

h = np.array([[1,0],
                [0,1]])

x = np.array([[0,1],
              [1,0]])

y = np.array([[0,1],
              [-1,0]])

z = np.array([[1,0],
              [0,-1]])

print("Operatory: \n u = 1^ \n h = 1/2 1^ \n x = Ix^ \n y = Iy^ \n z = Iz^")

#Program počítá až čtyři operátory
pocet_operatoru = int(input("Kolik operátorů budeš násobit? "))
if pocet_operatoru > 4:
    print("To je až příliš moc kamaráde...")
    exit()

#Pro přímý součin matic (Dirac product, direct product) jsou využity proměnné 'a' a 'b'.
#Pro konstanty jsou využity proměnné 'c' a 'd'.
def produkt():
    prvni = input("Zadej prvni operator (jednotkovy, pul, x, y, z): ")
    if prvni == 'jednotkovy':
        a = jednotkovy
        c = 1
    if prvni == 'pul':
        a = pul
        c = konstanta_pul_x_z
    if prvni == 'x':
        a = x
        c = konstanta_pul_x_z
    if prvni == 'y':
        a = y
        c = konstanta_y
    if prvni == 'z':
        a = z
        c = konstanta_pul_x_z


    druhy = input("Zadej druhy operator (jednotkovy, pul, x, y, z): ")
    if druhy == 'jednotkovy':
        b = jednotkovy
        d = 1
    if druhy == 'pul':
        b = pul
        d = konstanta_pul_x_z
    if druhy == 'x':
        b = x
        d = konstanta_pul_x_z
    if druhy == 'y':
        b = y
        d = konstanta_y
    if druhy == 'z':
        b = z
        d = konstanta_pul_x_z
    vysledek_konstanta = (2*c*d)
    vysledek = np.einsum('ij,kl-> ijkl', a, b)

    while pocet_operatoru < 3:
        print("\n",vysledek_konstanta,"\n\n", vysledek)
        break
#Pro přímý součin matic (Dirac product, direct product) jsou využity proměnné 'ab' a 'e'.
#Pro konstanty jsou využity proměnné 'cd' a 'f'.
    else:
        treti = input("Zadej treti operator (jednotkovy, pul, x, y, z): ")
        if treti == 'jednotkovy':
            e = jednotkovy
            f = 1
        if treti == 'pul':
            e = pul
            f = konstanta_pul_x_z
        if treti == 'x':
            e = x
            f = konstanta_pul_x_z
        if treti == 'y':
            e = y
            f = konstanta_y
        if treti == 'z':
            e = z
            f = konstanta_pul_x_z
        vysledek_tri = np.einsum('ijkl,mn-> ijklmn', vysledek, e)
        vysledek_konstanta_tri = (3*c*d*f)
              

        while pocet_operatoru < 4:
            print("\n",vysledek_konstanta_tri,"\n\n", vysledek_tri)
            break
#Pro přímý součin matic (Dirac product, direct product) jsou využity proměnné 'abe' a 'g'.
#Pro konstanty jsou využity proměnné 'cdf' a 'h'.
        else:
            ctvrty = input("Zadej ctvrty operator (jednotkovy, pul, x, y, z): ")
            if treti == 'jednotkovy':
                g = jednotkovy
                h = 1
            if treti == 'pul':
                g = pul
                h = konstanta_pul_x_z
            if treti == 'x':
                g = x
                h = konstanta_pul_x_z
            if treti == 'y':
                g = y
                h = konstanta_y
            if treti == 'z':
                g = z
                h = konstanta_pul_x_z
            vysledek_ctyr = np.einsum('ijklmn,op-> ijklmnop', vysledek_tri, g)
            vysledek_konstanta_ctyr = (4*c*d*f*h)
            print("\n",vysledek_konstanta_ctyr,"\n\n", vysledek_ctyr)      


produkt()





