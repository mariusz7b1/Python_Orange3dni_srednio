

def moj_generator(n):
    # inicjalizacja
    var = 0

    # Petla
    while var < n:

        # zwraca aktualną wartosc
        yield var

        # inkrementacja licznika
        var += 1


# iteracja na wartosciach zwracanych przez generator

for wartosc in moj_generator(3):
    print(wartosc)


generator1 = moj_generator(3)

generator2 = moj_generator(4)

generator3 = moj_generator(5)


print(id(generator1), id(generator2), id(generator3))


print(next(generator1))  # 0
print(next(generator1))  # 1
print(next(generator1))  # 2
#print(next(generator1))  # blad


print(next(generator2))
print(next(generator2))
print(next(generator3))


lst1 = list(moj_generator(10))
print(lst1)
