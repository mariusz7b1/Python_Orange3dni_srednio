"""
Fun jako argument
"""


def mnoz(a, b):
    return a * b


def dziel(a, b):
    return a / b


def wykonaj_operacje(operacja, a, b):
    return operacja(a, b)


# Przypisanie funkcji do zmiennej
moja_funkcja = mnoz

# Przekazanie funkcji jako argumentu do innej funkcji
wynik1 = wykonaj_operacje(moja_funkcja, 5, 3)
print(f"Wynik mnożenia: {wynik1}")

# Zmiana przypisanej funkcji
moja_funkcja = dziel

# Ponownie przekazanie funkcji jako argumentu do innej funkcji
wynik2 = wykonaj_operacje(moja_funkcja, 10, 2)
print(f"Wynik dzielenia: {wynik2}")


for moja_funkcja in [mnoz, dziel]:
    print(wykonaj_operacje(moja_funkcja, 45, 15))
