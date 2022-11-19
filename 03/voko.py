from random import randrange
karta = randrange(2,11)
karta_krupier = randrange(2,11)
pokusy = range(1,12)
x=0
y=0
for _ in pokusy:
    karta = randrange(2,11)
    karta_krupier = randrange(2,11)
    x += karta
    y += karta_krupier
    chces_kartu = input("Chces kartu? ")
    if chces_kartu == 'Jo':
        chces_kartu = True
        if  chces_kartu:
                print("Tvoje karty: ", x ,", karty krupiera: " , y ,".")
                while x < 21 and y < 21 and chces_kartu:
                    dalsi = input("Chces dalsi? ")
                    if dalsi == 'Jo':
                        dalsi = True
                        if  dalsi:
                                karta = randrange(2,11)
                                karta_krupier = randrange(2,11)
                                x += karta
                                y += karta_krupier
                                print("Tvoje karty: ", x ,", karty krupiera: " , y ,".")
                        else:
                            if x > 21 and y < 21:
                                print("Tak tos posral kamo!")
                                exit()
                            if x > 21 and y > 21:
                                print("Oba jste to dosrali!")
                                exit()
                            if x == 21 and y != 21 and y < 21:
                                print("Gratz!")
                                exit()
                            if x != 21 and x<21 and y ==21:
                                print("Posrals to!")
                                exit()
                            if x < 21 and y > 21:
                                print("Vojebals ho!")
                                exit()
                            if x == 21 and y != 21 and y > 21:
                                print("Kokot dostal!")
                                exit()
                    else:
                        if x > y and x < 21:
                            print("Tvoje karty: ", x ,", karty krupiera: " , y ,".")
                            print("Dostal zmrdik!")
                            exit()

                        if y > x and y < 21:
                            print("Tvoje karty: ", x ,", karty krupiera: " , y ,".")
                            print("Vyjebal s tebou...")
                            exit()

                if x > 21 and y < 21:
                    print("Tak tos posral kamo!")
                    exit()
                if x > 21 and y > 21:
                    print("Oba jste to dosrali!")
                    exit()
                if x == 21 and y != 21 and y < 21:
                    print("Gratz!")
                    exit()
                if x != 21 and x<21 and y ==21:
                    print("Posrals to!")
                    exit()
                if x < 21 and y > 21:
                    print("Vojebals ho!")
                    exit()
                if x == 21 and y != 21 and y > 21:
                    print("Kokot dostal!")
                    exit()
    else:
        print("Tak jdi do prdele!")
        exit()