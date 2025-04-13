class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros_nyt = alinkerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros_nyt != kohde_kerros:
            if self.kerros_nyt < kohde_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros_nyt < self.ylinkerros:
            self.kerros_nyt += 1
            print(f"Hissi on nyt kerroksessa {self.kerros_nyt}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.kerros_nyt > self.alinkerros:
            self.kerros_nyt -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros_nyt}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

if __name__ == "__main__":
    hissi = Hissi(1, 12)
    try:
        uusi_kerros = int(input("Mihin kerrokseen haluat siirtyä? (1-12): "))
        print(f"Hissi siirtyy nyt kerrokseen {uusi_kerros}")
        hissi.siirry_kerrokseen(uusi_kerros)
        print("Hissi siirtyy takaisin alimpaan kerrokseen.")
        hissi.siirry_kerrokseen(1)
    except ValueError:
        print("Virhe: Syötä kelvollinen numero.")