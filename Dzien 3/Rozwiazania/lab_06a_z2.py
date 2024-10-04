# Zad 2: Użycie funkcji filter
from os import system
system("cls")


def dluzsze_niz_szesc_ver2(slowo):
    if len(slowo) > 6:
        return True
    else:
        return False


def dluzsze_niz_szesc(slowo):
    return len(slowo) > 6


def main():
    slowa = """Napisz program, który wczytuje listę słów i używa funkcji
    filter aby zwrócić listę słów dłuższych niż 6 znaków.""".split()

    przefiltrowane_slowa = list(filter(dluzsze_niz_szesc, slowa))
    print(przefiltrowane_slowa)

    przefiltrowane_slowa = list(filter(lambda x: len(x) > 6, slowa))
    print(przefiltrowane_slowa)


if __name__ == "__main__":
    main()
