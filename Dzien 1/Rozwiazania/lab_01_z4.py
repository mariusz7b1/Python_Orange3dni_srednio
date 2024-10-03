"""
Przykładowa relizacja:
Zadanie 6  z Laboratorium 03a
"""
from os import system
system('cls')

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
szukana_liczba = int(input("Podaj liczbę: "))
if szukana_liczba in liczby:
    print("Twoja liczba znajduje się na liście.")
else:
    print("Twoja liczba nie znajduje się na liście.")
