numerot = []
while True:
    numero = input("Anna numero: ")
    if numero =="":
        break
    try:
        numero = int(numero)
        numerot.append(numero)
    except ValueError:
        print("Yritä uudelleen ja anna kelvollinen luku.")
print("Pienin luku:",min(numerot), "suurin luku:",max(numerot))