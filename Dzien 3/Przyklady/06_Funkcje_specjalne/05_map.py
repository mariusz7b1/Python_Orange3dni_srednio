from os import system
system("cls")


"""
W Pythonie w wersji 2 funkcja map() zwraca listę,
w wersji 3 zwraca iterator, dlatego w tym przypadku w funkcji
multiple_hash konwertujemy go do listy za pomocą list().
"""

numbers = [7, 4, 9, 6, 8, 1]


def multiple_hash(multi):
    return "#"*multi


def pow2(war):
    return pow(2, war)


objekt_iterator = map(multiple_hash, numbers)
lst1 = list(objekt_iterator)
print(lst1)


objekt_iterator = map(pow2, numbers)
lst1 = list(objekt_iterator)
print(lst1)
