dny = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
for poradi, den in enumerate(dny):
    print(poradi+1, den)
print('_______________________')

for poradi, den in enumerate(dny, start=1):
    print(poradi, den)