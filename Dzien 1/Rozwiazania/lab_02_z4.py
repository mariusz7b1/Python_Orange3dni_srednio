

def read_float(prompt, min, max):
    assert isinstance(min, int) or isinstance(min, float), "parametr min musi być liczbą"
    assert isinstance(max, int) or isinstance(max, float), "parametr max musi być liczbą"

    while True:
        try:
            wartosc = float(input(prompt + " "))
        except ValueError:
            print("podaj liczbę !!!! złożoną z cyfr i \
                  maksymalknie jednej '.' ")
        except KeyboardInterrupt:
            print(" Nic z tego  :)")
        else:
            if wartosc < min or wartosc > max:
                print(f"zły zakres !!! Podaj liczbę od {min} do {max}")
            else:
                break
    return wartosc


def main():
    print(read_float("Podaj liczbę rzeczywistą", 1, 5))


if __name__ == "__main__":
    main()
