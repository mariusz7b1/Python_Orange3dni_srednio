# Zad. 3: Użycie funkcji enumerate
from os import system
system("cls")

slowa = ['jabłko', 'banan', 'pomarańcza']

for indeks, slowo in enumerate(slowa):
    print(f'{indeks}: {slowo}')
