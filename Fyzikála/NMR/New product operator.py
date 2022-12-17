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

poradi = list(input('Napište operátory v patřičném pořadí: '))
for i in poradi:
    if i == " ":
        poradi.remove(" ")
for 1 in poradi:
    if i == "u":
        a = u
    if i == "h":
        a = h
    if i == "x":
        a = x
    if i == "y":
        a = y
    if i == "z":
        a = z


print(poradi)