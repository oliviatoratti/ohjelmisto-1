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

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissit_lkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = []
        for i in range(1, hissit_lkm + 1):
            self.hissit.append(Hissi(i))

    def aja_hissiä(self, hissin_nro, kohdekerros):
        if hissin_nro < 1 or hissin_nro > self.hissit:
            print("Hissin numero on virheellinen.")
            return
        if kohdekerros < self.alinkerros or kohdekerros > self.ylinkerros:
            print("Kohdekerros on virheellinen.")
            return
        self.hissit[hissin_nro - 1].aja(kohdekerros)

if __name__ == "__main__":
    talo = Talo(1, 6, 3)
    talo.aja_hissiä(1, 5)
    talo.aja_hissiä(3, 2)
    talo.aja_hissiä(4, 3)
    talo.aja_hissiä(2, 7)