"""Rozwiązanie zadania 1 z listy 3a   wersja tradycyjna"""
from sys import exit as exit_prog
from os import system
# czyszczenie ekranu
system("cls")
# Definiowanie samogłosek
SAMOGLOSKI = "aeiouyAEIOUY"


def main():
    in_file_name = "ksiazka.txt"
    out_file_name = "raport-b.txt"
    file_path = "d:\\dane\\"

    try:
        # otwarcie pliku do odczytu
        f_in = open(file_path + in_file_name, "rt", encoding="utf-8")
    except IOError:
        print("Nie udało się otworzyć pliku do odczytu")
        exit_prog()
    try:
        # otwarcie pliku do zapisu
        f_out = open(file_path + out_file_name, "wt", encoding="utf-8")
    except IOError:
        print("Nie udało się otworzyć pliku do zapisu")
        f_in.close()  # nie jest to konieczne
        exit_prog()

    tekst = f_in.read()
    liczba_a = tekst.count('a')
    rozne_znaki = set(tekst)

    liczba_samoglosek = 0
    for samogloska in SAMOGLOSKI:
        liczba_samoglosek = liczba_samoglosek + tekst.count(samogloska)

    # Otwarcie pliku do zapisu

    f_out.write(f"Liczba wystąpień litery 'a': {liczba_a}\n")
    f_out.write(f"Liczba różnych znaków: {len(rozne_znaki)}\n")
    f_out.write(f"Liczba wystąpień samogłosek: {liczba_samoglosek}\n")

    f_in.close()
    f_out.close()
    print("Zakonczone z sukcesem")


main()
