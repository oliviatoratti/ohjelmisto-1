import requests

käynnistys = input("Paina Enter ja saat Chuck Norris -vitsin")
pyyntö = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print("Tässä vitsi: \n")
        print(json_vastaus["value"])

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
except Exception as ex:
    print("Tapahtui odottamaton virhe")