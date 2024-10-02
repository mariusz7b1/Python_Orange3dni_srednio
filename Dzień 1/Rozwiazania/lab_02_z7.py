from random import randint
from os import system


def read_int(prompt, min, max):
    while True:
        try:
            wartosc = int(input(prompt+" "))
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


def test_random_generator(n, od, do) -> None:

    assert n <= 10000, "n musi być mniejsza od 100000"
    assert od < do, "od musi być mniejsza od do"

    lst = [randint(od, do) for i in range(n)]
    wynik = [(lst.count(i)) for i in range(od, do+1)]

    print(f"Przetestowano {n} liczb z zakresu {od} {do}")
    print("wyniki zamieszczono w poniższej tabeli")
    wynik_proc = [((wynik[i]/n*100)) for i in range(do)]

    for i in range(od, do+1):
        print(f"{i:4} wystapiło {wynik_proc[i-1]:>6.2f} % ")


def main() -> None:
    system("cls")
    n = read_int("Podaj liczbę liczb do generowania: ", 100, 10000)
    od = read_int("Podaj minimalną liczbę: ", 1, 999)
    do = read_int("Podaj maksymalną liczbę: ", od+1, 1000)
    test_random_generator(n, od, do)


if __name__ == "__main__":
    main()
