print('I heard this poem: ')
print()

with open('poem.txt', encoding = 'utf-8') as file:
    for x in file:
        print('     ' + x, end='')

print('\n')

with open('poem.txt', encoding = 'utf-8') as file:
    for x in file:
        x = x.rstrip()
        print('     ' + x)


print()
print('You like it?')