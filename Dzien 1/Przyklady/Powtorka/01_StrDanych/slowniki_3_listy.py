"""
Listy i słowniki w Pythonie
"""

import csv
from os import system
from sys import exit as exit_prog
system("cls")

# odczyt z pliku
file_in = 'c:\\dane\\users.csv'


try:
    f_in = open(file_in, "rt", encoding="utf-8")
except IOError:
    print("Błąd odczytu/zapisu z/do pliku:")
    exit_prog()


reader = csv.reader(f_in, delimiter=',',)
lista_osob = []
for rekord in reader:
    dct = {}
    # print(id(dct))
    # odczytaj z pliku kolejną linie
    dct["imie"] = rekord[4]
    dct["nazwisko"] = rekord[5]
    dct["miasto"] = rekord[6]
    lista_osob.append(dct)

print(lista_osob[1])
f_in.close()
