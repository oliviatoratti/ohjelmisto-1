oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa.")
        break
    else:
        yritykset += 1
        if yritykset < 5:
            print(f"Väärä salasana tai käyttäjätunnus. Yritä uudelleen. Yrityksiä on jäljellä: {5 - yritykset}.")
        else:
            print("Pääsy evätty.")