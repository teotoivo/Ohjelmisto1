import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntia):
        matkustettu_matka = self.tamanhetkinen_nopeus * tuntia
        self.kuljettu_matka += matkustettu_matka


# Pääohjelma
# Luodaan 10 autoa listaan
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus 100-200 km/h välillä
    autot.append(Auto(rekisteritunnus, huippunopeus))

# Kilpailu alkaa
kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        # Arvotaan nopeuden muutos -10 ja +15 km/h välillä
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        # Kuljetaan yksi tunti
        auto.kulje(1)

        # Tarkistetaan, onko jokin auto saavuttanut 10000 km
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

# Tulostetaan tulokset
print(f"{'Rekisteritunnus':<12}{'Huippunopeus':<15}{'Nopeus':<10}{'Kuljettu matka':<15}")
for auto in autot:
    print(
        f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<15}{auto.tamanhetkinen_nopeus:<10}{auto.kuljettu_matka:<15.2f}")
