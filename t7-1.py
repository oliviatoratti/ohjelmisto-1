vuodenajat = {1:"talvi", 2:"talvi", 3:"kevät", 4:"kevät", 5:"kevät", 6:"kesä", 7:"kesä", 8:"kesä", 9:"syksy", 10:"syksy", 11:"syksy", 12:"talvi"}
kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1 <=kuukausi <=12:
    print(f"Vuodenaika on: {vuodenajat[kuukausi]}.")