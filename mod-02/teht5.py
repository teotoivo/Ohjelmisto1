
def luotiGramma(luotia):
    return luotia * 13.3
def naulaGrammaa(naulaa):
    return luotiGramma(naulaa * 32)
def leiviskäGrammaa(leiviskää):
    return naulaGrammaa(leiviskää * 20)
def gToText(g):
    return str(g // 1000) + " kilogrammaa ja " + str(g % 1000) + " grammaa."

leiviskät = input("Anna leiviskät: ")
leiviskät = float(leiviskät)

naulat = input("Anna naulat: ")
naulat = float(naulat)

luodit = input("Anna luodit: ")
luodit = float(luodit)

print("Massa nykymittojen mukaan:")
print(gToText((leiviskäGrammaa(leiviskät) + naulaGrammaa(naulat) + luotiGramma(luodit))))