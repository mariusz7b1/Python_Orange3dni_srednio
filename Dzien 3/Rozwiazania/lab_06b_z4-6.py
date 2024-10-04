# zad 4 enumerate
slowa = "To jest kurs Phyton i uczymy się funkcji wyzszego rzedu".split()
slownik_indeksow = {slowo: indeks for indeks, slowo in enumerate(slowa)}
print(slownik_indeksow)


# zad 5 enumerate
klucze = "To jest kurs Phyton i uczymy się funkcji wyzszego rzedu".split()
wartosci = [len(war) for war in klucze]
slownik = dict(zip(klucze, wartosci))
print(slownik)

# zad 6 map,zip
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
sumy = list(map(lambda x: x[0] + x[1], zip(lista1, lista2)))
print(sumy)
