class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohde_kerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei ole kelvollinen.")

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for index, hissi in enumerate(self.hissit):
            print(f"Siirretään hissi {index} pohjakerrokseen.")
            hissi.siirry_kerrokseen(self.alin_kerros)

# Testataan ohjelmaa
if __name__ == "__main__":
    talo = Talo(1, 10, 3)  # Luodaan talo, jossa on 3 hissiä ja kerrokset 1–10
    talo.aja_hissiä(0, 5)  # Ajetaan ensimmäinen hissi kerrokseen 5
    talo.aja_hissiä(1, 3)  # Ajetaan toinen hissi kerrokseen 3
    talo.aja_hissiä(2, 7)  # Ajetaan kolmas hissi kerrokseen 7
    talo.palohälytys()     # Käynnistetään palohälytys, jolloin kaikki hissit siirtyvät pohjakerrokseen
