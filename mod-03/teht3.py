sukupuoli = input("Anna sukupuoli (m/n): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "m":
    if hemoglobiiniarvo < 134:
        print("liian pieni")
    elif hemoglobiiniarvo > 195:
        print("liian suuri")
    else:
        print("ok")
elif sukupuoli == "n":
    if hemoglobiiniarvo < 117:
        print("liian pieni")
    elif hemoglobiiniarvo > 175:
        print("liian suuri")
    else:
        print("ok")