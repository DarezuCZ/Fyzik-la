kapaliny = [['voda', 100, 'H2O'], 
            ['toluen', 110, 'C7H8']]
print(kapaliny)

soucin = (int(kapaliny[0][1]))*(int(kapaliny[1][1]))
print(soucin)

kapaliny[0].append('tekutina')
print(kapaliny)

for _ in kapaliny[0]:
    print('LOL')