# zad  7 filter
liczby = list(range(1, 101))
wielokrotnosci = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, liczby))
print(wielokrotnosci)

# zad  8 enumeratye,zip

# lista 1 to unikalne male znaki + spacja z podanego ciagu znaków
lista1 = set(list("Ala ma psa i kota ".lower()))
# lista 2 to liczby parzyste tyle ile ma dlugosci ciag znakow
lista2 = [i for i in range(0, len(lista1)*2) if i % 2 == 0]

wynik = tuple(map(lambda x: (x[0], x[1]), enumerate(zip(lista1, lista2))))
print(wynik)


lista1 = ["Python", "kurs", "programowanie"]
lista2 = ["Python", "kurs", "test"]
dlugosci = list(map(lambda x: len(x), filter(lambda x: x in lista1, lista2)))


liczby = [10, 20, 30, 40, 50]
wynik = list(map(lambda x: x[1] - x[0], enumerate(liczby)))
