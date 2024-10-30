from os import system
system("cls")

lista_krotek = [(1, 2), (3, 1), (2, 3), (4, 2)]


def sortuj(war):
    return war[1]
# Użyj funkcji lambda do sortowania listy
# według drugiego elementu każdej krotki


lista_krotek.sort(key=sortuj)

print(lista_krotek)  # Wyświetli: [(3, 1), (1, 2), (4, 2), (2, 3)]

pass

lista_krotek.sort(key=lambda element: element[1])
print(lista_krotek)  # Wyświetli: [(3, 1), (1, 2), (4, 2), (2, 3)]


def mnoznik(n):
    return lambda x: x * n


podwajacz = mnoznik(2)
"podwajacz=lambda x: x * 2"
potrajacz = mnoznik(3)
"potrajacz=lambda x: x * 3"

print(type(podwajacz))
print(type(potrajacz))

print(podwajacz(5))  # Wyświetli: 10
print(potrajacz(5))  # Wyświetli: 15
