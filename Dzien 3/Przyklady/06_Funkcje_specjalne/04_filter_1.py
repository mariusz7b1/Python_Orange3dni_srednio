"""
funkcja filter(); składnia :  filter(function, iterable)
"""
from os import system
system("cls")

liczby = list(range(1, 21))


# zwraca True jesli parzysta

def sprawdz_parzyste(liczba):
    if liczba % 2 == 0:
        return True

    return False


# zastosowanie funkcji filter
parzyste_iterator = filter(sprawdz_parzyste, liczby)
print(type(parzyste_iterator))

# zmiana iteratora na liste
liczby_parzyste = list(parzyste_iterator)

print(liczby_parzyste)
