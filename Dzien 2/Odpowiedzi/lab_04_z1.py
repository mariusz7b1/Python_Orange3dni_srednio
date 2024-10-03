"""
Przykładowe rozwiąznie zadania 1 z listy 4
"""

from os import system
system("cls")


def kwadrat(limit):
    for liczba in range(1, limit + 1):
        yield liczba ** 2


for liczba2 in kwadrat(5):
    print(liczba2)
