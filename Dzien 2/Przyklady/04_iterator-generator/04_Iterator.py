"""
Iteratory 
"""


def wypisz_elementy(lista_elementow):
    iterator = iter(lista_elementow)
    print(type(iterator))
    try:
        while True:
            element = next(iterator)
            print(element)
    except StopIteration:
        print("Koniec listy elementów.")


def wypisz_litery(napis):
    iterator_napisu = iter(napis)
    print(type(iterator_napisu))
    try:
        while True:
            litera = next(iterator_napisu)
            print(litera)
    except StopIteration:
        pass


lista_ksiazek = ["Czysty kod", (1, 2, 3), "Wzorce projektowe"]
wypisz_elementy(lista_ksiazek)

wypisz_litery("Witaj Świecie!")
