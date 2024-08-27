while True:
    tuuma = input("Anna tuuma: ")
    if int(tuuma) < 0:
        break
    print("Senttimetreinä:", int(tuuma) * 2.54)