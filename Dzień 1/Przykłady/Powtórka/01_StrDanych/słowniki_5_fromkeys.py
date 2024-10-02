from os import system
system("cls")


klucze = ['klucz1', 'klucz2', 'klucz3']
nowy_slownik = dict.fromkeys(klucze)
print(nowy_slownik)


s1 = "ala ma kota i co z tego"
s1 = s1.replace(" ", "")

# ver 1
zmienna_robocza = set(s1)
print(zmienna_robocza)
zmienna_robocza = list(zmienna_robocza)
zmienna_robocza.sort()
dct1 = dict.fromkeys(zmienna_robocza, 0)
print(dct1)

# ver 2
dct1 = dict.fromkeys(sorted(list(set(s1))), 0)
print(dct1)

# ver 3
dct1 = dict.fromkeys(sorted(s1), 0)
print(dct1)
