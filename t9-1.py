class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

def Main():
    auto = Auto("ABC-123", 142)
    print(f"Auton ominaisuudet: ")
    print(f"- rekisteritunnus: {auto.rekisteritunnus}")
    print(f"- huippunopeus: {auto.huippunopeus} km/h")
    print(f"- nopeus nyt: {auto.nopeus_nyt} km/h")
    print(f"- kuljettu matka: {auto.kuljettu_matka} kilometriä")

if __name__ == "__main__":
    Main()