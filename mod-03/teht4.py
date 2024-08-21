vuosi = input("Anna vuosi: ")

if int(vuosi) % 4 == 0:
    if int(vuosi) % 100 == 0:
        if int(vuosi) % 400 == 0:
            print("Vuosi on karkausvuosi.")
        else:
            print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")