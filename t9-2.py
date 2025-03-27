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

def main():
    auto = Auto("ABC-123", 142)
    auto.kiihdytä(+30)
    print(f"Tämänhetkinen nopeus: {auto.nopeus_nyt} km/h")
    auto.kiihdytä(+70)
    print(f"Tämänhetkinen nopeus: {auto.nopeus_nyt} km/h")
    auto.kiihdytä(+50)
    print(f"Tämänhetkinen nopeus: {auto.nopeus_nyt} km/h")
    auto.kiihdytä(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus_nyt} km/h")

if __name__ == "__main__":
    main()