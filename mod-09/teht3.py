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

    def kulje(self, tuntia):
        # Lasketaan matka, jonka auto kulkee annetussa tuntimäärässä
        matkustettu_matka = self.tamanhetkinen_nopeus * tuntia
        self.kuljettu_matka += matkustettu_matka

# Pääohjelma
auto = Auto("ABC-123", 142)

# Kiihdytetään autoa
auto.kiihdyta(60)
print(f"Tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus} km/h")

# Kuljettu matka ennen ajoa
print(f"Kuljettu matka ennen ajoa: {auto.kuljettu_matka} km")

# Kuljetaan 1.5 tuntia
auto.kulje(1.5)

# Tulostetaan kuljettu matka ajon jälkeen
print(f"Kuljettu matka ajon jälkeen: {auto.kuljettu_matka} km")
