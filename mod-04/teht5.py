käyttäjä = "python"
salasana = "rules"

wrongCounter = 0

while True:
    if wrongCounter >= 5:
        print("Liikaa yrityksiä")
        break
    userInput = input("Anna käyttäjätunnus: ")
    passInput = input("Anna salasana: ")
    if userInput == käyttäjä and passInput == salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana")
        wrongCounter += 1
        continue
