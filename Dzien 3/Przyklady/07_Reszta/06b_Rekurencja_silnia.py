"""
Rekurencja cd
"""


def silnia(liczba):
    if liczba == 0 or liczba == 1:
        return 1
    else:
        return liczba * silnia(liczba - 1)


wartosc = int(input("Podaj liczbę ? "))
# wwalidacja danych
wynik = silnia(wartosc)
print(f"Silnia dla liczby {wartosc} wynosi {wynik}")
