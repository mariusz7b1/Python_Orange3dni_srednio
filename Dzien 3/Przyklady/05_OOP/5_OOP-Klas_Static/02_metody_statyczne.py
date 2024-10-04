"""
staticmethod to metoda statyczna, która nie operuje ani na klasie, ani na instancji, 
a po prostu jest funkcją związaną z klasą.
"""


class Kalkulator:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b

    @staticmethod
    def pomnoz(a, b):
        return a * b

    @staticmethod
    def podziel(a, b):
        if b == 0:
            return "Nie można dzielić przez zero!"
        return a / b


# Użycie metod statycznych
print(Kalkulator.dodaj(5, 3))  # Wynik: 8
print(Kalkulator.odejmij(10, 3))  # Wynik: 7
print(Kalkulator.pomnoz(4, 3))  # Wynik: 12
print(Kalkulator.podziel(8, 2))  # Wynik: 4.0
print(Kalkulator.podziel(8, 0))  # Wynik: Nie można dzielić przez zero!
