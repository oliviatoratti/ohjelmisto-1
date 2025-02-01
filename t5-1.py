import random
nopat = int(input("Anna noppien lukumäärä: "))
summa = 0
for _ in range(nopat):
    noppa = random.randint(1, 6)
    summa += noppa
print("Silmälukujen summa: ")
print(summa)