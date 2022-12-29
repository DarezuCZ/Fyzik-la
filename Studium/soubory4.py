with open('numbers to add.txt', encoding='utf-8') as soubor:
    cisla = []
    i = 0
    for x in soubor:
        cisla.append(int(x))
        i = i+int(x)
    print(cisla)
    print((cisla[0])+(cisla[1]))
    print(i)