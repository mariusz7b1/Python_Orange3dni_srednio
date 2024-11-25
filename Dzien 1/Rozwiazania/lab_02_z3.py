""""
Funckcja read_int
"""


def read_int(prompt="podaj liczbę całkowitą", minimum=0, maksimum=100):
    assert isinstance(minimum, int), "parametr min musi być liczbą całkowitą"
    assert isinstance(maksimum, int), "parametr max musi być liczbą całkowitą"
    prompt = f"{prompt} (od {minimum} do {maksimum}):  "
    while True:
        try:
            wartosc = int(input(prompt + " "))
        except ValueError:
            print("podaj liczbę !!!! złożoną z cyfr ")
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
    print(read_int("Podaj liczbę całkowitą", 1, 5))
    print(read_int("Podaj wiek ", 18, 110))
    print(read_int("Podaj ilosć prób", 100, 200))


if __name__ == "__main__":
    main()
