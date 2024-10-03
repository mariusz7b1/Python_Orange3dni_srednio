from os import system
from random import randint
system("cls")

# deklaracja słownika i listy
lista_osob = []

# wczytywanie danych
zm_robocza = 1


while zm_robocza <= 5:
    dct = {}
    print(id(dct))
    # odczytaj z pliku kolejną linie
    dct["imie"] = "Jan_" + str(zm_robocza)          # najcześciej dane z pliku
    dct["nazwisko"] = "Nowak_" + str(zm_robocza)
    dct["wiek"] = randint(20, 90)
    lista_osob.append(dct)
    zm_robocza += 1

record = (lista_osob[-2])["nazwisko"]

print(record)
