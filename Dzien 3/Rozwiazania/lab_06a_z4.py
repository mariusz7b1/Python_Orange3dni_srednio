# Zad. 4: Użycie funkcji zip
from os import system
system("cls")

imiona = ['Alicja', 'Bartek', 'Karol']
wiek = [25, 30, 35]

spakowane = tuple(zip(imiona, wiek))
print(spakowane)
