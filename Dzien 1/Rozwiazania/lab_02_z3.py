def read_int(prompt="podaj liczbę całkowitą", min=0, max=100):
    assert isinstance(min, int), "parametr min musi być liczbą całkowitą"
    assert isinstance(max, int), "parametr max musi być liczbą całkowitą"
    while True:
        try:
            wartosc = int(input(prompt + " "))
        except ValueError:
            print("podaj liczbę !!!! złożoną z cyfr ")
        except KeyboardInterrupt:
            print(" Nic z tego  :)")
        else:
            if wartosc < min or wartosc > max:
                print(f"zły zakres !!! Podaj liczbę od {min} do {max}")
            else:
                break
    return wartosc


def main():
    print(read_int("Podaj liczbę całkowitą", 1, 5))
    print(read_int("Podaj liczbę całkowitą", "", 5))


if __name__ == "__main__":
    main()
