def parittomat(luku_lista):
    karsittu_lista = []
    for luku in luku_lista:
        if luku % 2 == 0:
            karsittu_lista.append(luku)
    return karsittu_lista
def main():
    luku_lista = [8, 3, -9, 2, 17, 28]
    karsittu_lista = parittomat(luku_lista)
    print("Alkuperäinen lista:", luku_lista)
    print("Karsittu lista:", karsittu_lista)
main()