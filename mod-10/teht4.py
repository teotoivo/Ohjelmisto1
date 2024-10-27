import random

class Auto:
    def __init__(self, nimi, nopeus, matka=0):
        self.nimi = nimi
        self.nopeus = nopeus
        self.matka = matka

    def kulje(self):
        self.matka += self.nopeus

    def muuta_nopeutta(self):
        # Auton nopeuden satunnainen muutos välillä -10 ja +10 km/h
        nopeuden_muutos = random.randint(-10, 10)
        self.nopeus = max(0, self.nopeus + nopeuden_muutos)  # Varmistetaan, että nopeus ei mene negatiiviseksi

class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autolista

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.muuta_nopeutta()  # Arvotaan uusi nopeus
            auto.kulje()           # Auto kulkee nykyisellä nopeudella

    def tulosta_tilanne(self):
        print(f"{'Auto':<20} {'Nopeus (km/h)':<15} {'Matka (km)':<10}")
        print("-" * 45)
        for auto in self.autot:
            print(f"{auto.nimi:<20} {auto.nopeus:<15} {auto.matka:<10}")
        print("-" * 45)

    def kilpailu_ohi(self):
        # Tarkistetaan, onko joku autoista saavuttanut kilpailun pituuden
        return any(auto.matka >= self.pituus_km for auto in self.autot)

# Pääohjelma
if __name__ == "__main__":
    # Luodaan lista autoista
    autot = [Auto(f"Auto {i+1}", random.randint(100, 200)) for i in range(10)]

    # Luodaan 8000 km kilpailu nimeltä "Suuri romuralli"
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    tunti = 0

    # Kilpailun simulointi
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1

        # Tulostetaan tilanne joka kymmenes tunti
        if tunti % 10 == 0:
            print(f"\nTilanne {tunti} tunnin jälkeen:")
            kilpailu.tulosta_tilanne()

    # Kilpailu on päättynyt, tulostetaan lopputilanne
    print("\nKilpailu on päättynyt!")
    kilpailu.tulosta_tilanne()
