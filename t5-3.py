onAlku = True
luku = int(input("Anna kokonaisluku: "))
for jakaja in range(2, luku):
    if luku % jakaja == 0:
        onAlku = False
        break
if (onAlku == True):
    print("Lukusi on alkuluku")
else:
    print("Lukusi ei ole alkuluku")