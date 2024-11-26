"""
Przykładowe rozwiąznie zadania 2 z listy 4
"""

from os import system
system("cls")


def cz_pierwsza(n):
    if n <= 1:
        return False
    # Sprawdzenie dla liczby 2
    if n == 2:
        return True
    # Wykluczenie liczb parzystych większych niż 2
    if n % 2 == 0:
        return False

    # Sprawdzamy dzielniki do sqrt(n)
    for i in range(3, int(n**2) + 1, 2):
        if n % i == 0:
            return False
    return True


def liczby_pierwsze(start, end):
    for liczba in range(start, end + 1):
        if cz_pierwsza(liczba):
            yield liczba


def main():
    print("no to start ")
    for pierwsza in liczby_pierwsze(100, 1000):
        print(pierwsza)


if __name__ == "__main__":
    main()
