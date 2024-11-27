"""
Fun jako argument
"""


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def mnoz(a, b):
    return a * b


def dziel(a, b):
    return a / b


def wykonaj_operacje(dzialanie, a, b):
    return dzialanie(a, b)


# Przypisanie funkcji do zmiennej
moja_funkcja = [("dodawanie", dodaj), ("odejmowanie", odejmij),
                ("mnożenie", mnoz), ("dzielenie", dziel)]

# Przekazanie funkcji jako argumentu do innej funkcji
for operacja, fun in moja_funkcja:
    wynik1 = wykonaj_operacje(fun, 15, 3)
    print(f"Wynik opercaji {operacja}: {wynik1}")
