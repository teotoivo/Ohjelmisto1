class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        # Tarkistetaan, että nopeus ei ylitä huippunopeutta eikä alita nollaa
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

# Pääohjelma
auto = Auto("ABC-123", 142)

# Kiihdytetään autoa annetuilla arvoilla
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus} km/h")

# Hätäjarrutus
auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")
