# zad 1 map
slowa = "To jest kurs Phyton i uczymy się funkcji wyzszego rzedu".split()
slowa_odwrocone = list(map(lambda slowo: slowo[::-1], slowa))
print(slowa_odwrocone)

# zad 2 filter
slowa = ["kajak", "Python", "oko", "kurs"]
palindromy = list(filter(lambda slowo: slowo == slowo[::-1], slowa))
