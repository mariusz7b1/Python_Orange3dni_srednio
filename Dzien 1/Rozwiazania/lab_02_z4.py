""""
Funkcja read_float
"""


def read_float(prompt, minimum, maksimum):
    assert isinstance(minimum, int, float), "parametr min musi być liczbą"
    assert isinstance(maksimum, int, float), "parametr max musi być liczbą"
    prompt = f"{prompt} (od {minimum} do {maksimum}):  "
    while True:
        try:
            wartosc = float(input(prompt + " "))
        except ValueError:
            print("podaj liczbę !!!! złożoną z cyfr i \
                  maksymalknie jednej '.' ")
        except KeyboardInterrupt:
            print(" Nic z tego  :)")
        else:
            if wartosc < minimum or wartosc > maksimum:
                print(f"zły zakres !!! Podaj liczbę od {
                      minimum} do {maksimum}")
            else:
                break
    return wartosc


def main():
    print(read_float("Podaj liczbę rzeczywistą", 1, 5))


if __name__ == "__main__":
    main()
