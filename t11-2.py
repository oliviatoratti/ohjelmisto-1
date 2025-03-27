class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus_nyt + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus_nyt = 0
        else:
            self.nopeus_nyt = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus_nyt * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
    def __str__(self):
        return f"{self.rekisteritunnus} - sähköauto, huippunopeus: {self.huippunopeus} km/h, akkukapasiteetti {self.akkukapasiteetti} kWh."

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_koko = bensatankki_koko
    def __str__(self):
        return f"{self.rekisteritunnus} - polttomoottoriauto, huippunopeus: {self.huippunopeus} km/h, bensatankin koko {self.bensatankki_koko} litraa"

def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    sähköauto.kiihdytä(80)
    sähköauto.kulje(3)
    polttomoottoriauto.kiihdytä(80)
    polttomoottoriauto.kulje(3)
    print(f"Sähköauton kulkema matka on {sähköauto.kuljettu_matka} kilometriä")
    print(f"Polttomoottoriauton kulkema matka on {polttomoottoriauto.kuljettu_matka} kilometriä")

if __name__ == "__main__":
    main()