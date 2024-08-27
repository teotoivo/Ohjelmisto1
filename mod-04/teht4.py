import random

randomLuku = random.randint(1, 10)

while True:
    arvaus = input("arvaa luku 1-10: ")
    if int(arvaus) == randomLuku:
        print("Oikein!")
        break
    elif int(arvaus) < randomLuku:
        print("Luku on suurempi")
    else:
        print("Luku on pienempi")