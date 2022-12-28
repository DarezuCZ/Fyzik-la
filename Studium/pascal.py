
radky = range(int((((int(input('Napiš počet řádků: ')))*2)+1)/2))
sloupce = radky
prvky_trojuhelniku = []

for x in radky:
    for y in radky:
        prvky_trojuhelniku.append(x+y)

print(prvky_trojuhelniku)
for x in radky:
    print(prvky_trojuhelniku[1:(x)])