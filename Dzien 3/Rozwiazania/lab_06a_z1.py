# Zad 1: Użycie funkcji map
from os import system
system("cls")


def kwadrat(x):
    return x**2


def main():

    liczby = [1, 2, 3, 4, 5]

    # podejscie standardowe
    liczby_kwadratowe = []
    for ele in liczby:
        liczby_kwadratowe.append(kwadrat(ele))
    print(liczby_kwadratowe)

    # podejscie z map
    liczby_kwadratowe = list(map(kwadrat, liczby))
    print(liczby_kwadratowe)

    # podejscie z map i lambda
    liczby_kwadratowe = list(map(lambda x: x**2, liczby))
    print(liczby_kwadratowe)


if __name__ == "__main__":
    main()
