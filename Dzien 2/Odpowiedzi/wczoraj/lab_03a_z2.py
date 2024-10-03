"""
Zad 2 z listy 3a
"""
from sys import exit as exit_prog


def sortuj_slow(war):   # war= ("a",12)
    return war[1]


def sortuj_list(war):
    return len(war)


def czysc_slowo(slowo):
    slowo = slowo.strip()
    while len(slowo) > 0 and not slowo[0].isalpha():
        slowo = slowo[1:]
    while len(slowo) > 0 and not slowo[-1].isalpha():
        slowo = slowo[:-1]
    slowo = slowo.lower()
    return slowo


def main():
    try:
        f_in = open('d:\\dane\\ksiazka.txt', 'rt', encoding='utf-8')
        f_out = open('d:\\dane\\raport2.txt', 'wt', encoding='utf-8')
    except IOError:
        print("Wystąpił błąd podczas próby otwarcia/zapisu pliku.")
        exit_prog()

    slownik_liter = {}
    list_slow = []

    # wczytuje kolejna linie
    linia = f_in.readline()
    # tak dlugo jak mam co czytac
    while len(linia) != 0:
        # zamieniam na male litery
        linia = linia.lower()
        # wycinam ewentualne spacje , choć split to zrobi ale :)
        linia = linia.strip()
        # po słowach w linii i jak dluższe niż 3 to dodaję do słownika
        for slowo in linia.split():
            slowo = czysc_slowo(slowo)
            if 3 <= len(slowo) <= 30 and slowo.isalpha():
                list_slow.append(slowo)
        # dla każdej litery w lini
        for litera in linia:
            # jeśli jest to litera
            if litera.isalpha():
                # jesli nowa to dodaj element słownika i ustal wartość na 1
                if litera not in slownik_liter:
                    slownik_liter[litera] = 1
                else:
                    # Inkrementujemy wartość litery o 1
                    slownik_liter[litera] += 1
        linia = f_in.readline()

    # Wyświetlamy procentową częstotliwość wystąpienia każdej litery
    calkowita_liczba_liter = sum(slownik_liter.values())

    # Sortowanie po wartościach

    lista_liter = sorted(slownik_liter.items(), key=sortuj_slow, reverse=True)
    # alternatywa z zastosowaniem lambda
    # lista_liter = sorted(slownik_liter.items(),key=lambda x: x[1],
    # reverse=True)

    # Wyświetlamy statystykę
    for litera, liczba_wystąpień in lista_liter:
        procent = 100 * liczba_wystąpień / calkowita_liczba_liter
        str1 = f"Litera {litera}:{liczba_wystąpień} {procent:.2f}%"
        print(str1)
        f_out.write(str1 + "\n")

    str1 = f"Calkowita_liczba_liter w tekscie: {calkowita_liczba_liter}"
    print(str1)
    f_out.write(str1 + "\n")

    # slowa unikalne
    lista_slow_unik = list(set(list_slow))
    str1 = f"Ilosc unikalnych slow: {len(lista_slow_unik)}"
    print(str1)
    f_out.write(str1 + "\n")

    # Sortowanie po dlugosci słow
    lista_slow_unik.sort(key=sortuj_list, reverse=True)
#    lista_slow_unik.sort(key=lambda x: len(x), reverse=True)

    najdluzsze = len(lista_slow_unik[0])
    lista_najdluzszych = [lista_slow_unik[0] + "\n"]
    licznik = 1
    while len(lista_slow_unik[licznik]) == najdluzsze:
        lista_najdluzszych.append(lista_slow_unik[licznik] + "\n")
        licznik += 1

    str1 = f"najdłuższe słowo ma {najdluzsze} i  takich słów jest {licznik}"
    print(str1)
    f_out.write(str1 + "\n")
    f_out.writelines(lista_najdluzszych)

    f_in.close()
    f_out.close()


main()
