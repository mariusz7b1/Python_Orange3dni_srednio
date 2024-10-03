"""aPrzykładowa Relizacja zadania z listy 02b
zadanie 3
"""
from os import system
system('cls')


c0 = int(input("Podaj liczbę "))
krok = 0
while c0 != 1:
    krok += 1
    if c0 % 2 == 0:
        c0 = c0/2
    else:
        c0 = 3*c0+1
    print(int(c0))
print("Liczba kroków ", krok)
