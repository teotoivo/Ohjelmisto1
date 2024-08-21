kuhanMinPituus = 37

kuhanPituus = input("Kuinka pitkä kala oli? ")
kuhanPituus = int(kuhanPituus)

if kuhanPituus < kuhanMinPituus:
    print(f"Kuha on {kuhanMinPituus - kuhanPituus} cm liian lyhyt. Laske kuha takaisin järveen.")
else:
    print ("Kuha on sopivan kokoinen. Voit ottaa sen talteen.")