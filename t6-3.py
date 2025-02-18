def gallonat_litroihin(gallonat):
    return gallonat * 3.785
def main():
    while True:
        gallonat = float(input("Syötä bensiinin määrä gallonassa: "))
        if gallonat < 0:
            print("Ohjelma lopetetaan.")
            break
        litrat = gallonat_litroihin(gallonat)
        print(f"{gallonat} gallonaa on {litrat} litraa.")
main()