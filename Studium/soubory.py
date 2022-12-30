file = open('poem.txt', encoding = 'utf-8')
obsah = file.read()

file.close()
print(obsah)

with open('poem.txt', encoding = 'utf-8') as file:
    obsah = file.read()

print(obsah)