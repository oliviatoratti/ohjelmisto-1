kaupungit = []
for i in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
while kaupunki == "":
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraavan kaupungin nimi: ")
print(kaupunki)