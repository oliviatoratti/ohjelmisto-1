def laske_summa(luku_lista):
    summa = 0
    for luku in luku_lista:
        summa += luku
    return summa
def main():
    luku_lista = [8, 3, -9, 2, 17, 28] # esimerkki numerot
    summa = laske_summa(luku_lista)
    print(f"Lukujen summa on: {summa}.")
main()