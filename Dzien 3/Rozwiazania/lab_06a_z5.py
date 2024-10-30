#  Zad 5: Użycie funkcji sorted z argumentem key
from os import system
system("cls")


def klucz_slowa(slowo):
    return len(slowo)


def main():
    slowa = ['jabłko', 'banan', 'kiwi', 'winogrono', 'pomarańcza']
    posortowane_slowa = sorted(slowa, key=klucz_slowa)
    print(posortowane_slowa)

    posortowane_slowa = sorted(slowa, key=lambda slowo: len(slowo))
    print(posortowane_slowa)


if __name__ == "__main__":
    main()
