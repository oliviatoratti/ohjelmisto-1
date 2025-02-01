luvut = []
while True:
    luku = input("Anna luku tai lopeta painamalla Enter: ")
    if luku == "":
        break
    try:
        luku = int(luku)
        luvut.append(luku)
    except ValueError:
        print("Luvun tulee olla kokonaisluku")
suurimmat = sorted(luvut, reverse=True)[:5]
print("Viisi suurinta lukua: ", suurimmat)