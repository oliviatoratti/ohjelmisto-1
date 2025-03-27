import random

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

def main():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100,200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)
    kilpailu_end = False
    tunti = 0
    while not kilpailu_end:
        tunti += 1
        for auto in autot:
            nopeuden_muutos = random.randint(-10,15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)
        for auto in autot:
            if auto.kuljettu_matka >= 10000:
                kilpailu_end = True
                break
    print(f"{'Rekisteritunnus':<15} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)'}")
    for auto in autot:
        print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<20} {auto.nopeus_nyt:<15} {auto.kuljettu_matka}")

if __name__ == "__main__":
    main()