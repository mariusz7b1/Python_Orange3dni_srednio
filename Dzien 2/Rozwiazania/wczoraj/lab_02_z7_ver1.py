"""
Przykładowe rozwiązanie zadania 6,7
"""
from random import randint
from os import system


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


def test_random_generator(n, od, do) -> None:

    assert n <= 10000, "n musi być mniejsza od 100000"
    assert od < do, "od musi być mniejsza od do"

    lst = [randint(od, do) for i in range(n)]
    wynik = {i: lst.count(i) for i in range(od, do+1)}

    print(f"Przetestowano {n} liczb z zakresu {od} {do}")
    print("wyniki zamieszczono w poniższej tabeli")
    wynik_proc = {i: wynik[i]/n*100 for i in range(od, do+1)}

    for klucz, wartosc in wynik_proc.items():
        print(f"{klucz:4} wystapiło {wartosc:>6.2f} % ")


def main() -> None:
    system("cls")
    n = read_int("Podaj liczbę liczb do generowania: ", 100, 10000)
    od = read_int("Podaj minimalną liczbę: ", 1, 999)
    do = read_int("Podaj maksymalną liczbę: ", od+1, 1000)
    test_random_generator(n, od, do)


if __name__ == "__main__":
    main()
