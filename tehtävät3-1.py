kuha = float(input("Anna kuhan pituus sentteinä: "))
minpituus = 37
sentit = (minpituus - kuha)
if kuha >= 37:
    print("Kuha on täyskasvuinen.")
if kuha <= 36:
    print("Laske kuha takaisin järveen. Kuha on {sentit} senttiä vaille täyskasvuista.")