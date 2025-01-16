#1
nimi = input("Mikä on nimesi?: ")
print(f"Hei {nimi}!")

#2
import math
sade_str = float( input("Mikä on säteen pituus?:"))
pintaala = math.pi * int(sade_str ** 2)
print(f"Pinta-ala on: {pintaala}")

#3
kanta_str = float( input("Mikä on suorakulmion kanta?:"))
korkeus_str = float( input("Mikä on suorakulmion korkeus?:"))
piiri = 2 * (korkeus_str + kanta_str)
pintaala = korkeus_str * kanta_str
print(f"Piiri on: {piiri}")
print(f"Pinta-ala on: {pintaala}")

#4
lukuA_str = input("anna kokonaisluku: ")
lukuA = int(lukuA_str)
lukuB = int( input("anna toinen luku: ") )
lukuC = int( input("anna kolmas luku: ") )
summa = lukuA + lukuB + lukuC
tulo = lukuA * lukuB * lukuC
keskiarvo = summa / 3
print(f"Lukujesi summa = {summa}")
print(f"Lukujesi tulo = {tulo}")
print(f"Lukujesi keskiarvo = {keskiarvo}")

#5
luoti = 13.3
naula = luoti * 32
leiviska = naula * 20
leiviska_str = float( input("Anna leiviskät: "))
naula_str = float( input("Anna naulat: "))
luoti_str = float( input("Anna luodit: "))
summa = luoti_str + naula_str + leiviska_str
print(f"Summa = {summa}")

#6
