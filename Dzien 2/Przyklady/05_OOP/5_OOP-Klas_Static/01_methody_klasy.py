
"""
classmethod to metoda, która działa na poziomie klasy, a nie konkretnej instancji. 
Jako pierwszy argument przyjmuje klasę (cls), 
co umożliwia jej dostęp do atrybutów i metod klasowych.
"""


class Licznik:
    licznik_instancji = 0

    def __init__(self):
        Licznik.licznik_instancji += 1  # zwiększamy wartość statycznej zmiennej
        self.atrybu1 = 0
        self.atrybu2 = 0

    @classmethod
    def pokaz_licznik(cls):
        print(f"Liczba utworzonych instancji: {cls.licznik_instancji}")


# Utworzenie instancji klasy Licznik
Licznik.pokaz_licznik()
obiekt1 = Licznik()
obiekt2 = Licznik()

# Wywołanie metody klasy, aby pokazać wartość statycznej zmiennej
Licznik.pokaz_licznik()  # Wynik: Liczba utworzonych instancji: 2

# Dostęp do statycznej zmiennej przez instancję
print(obiekt1.licznik_instancji)  # Wynik: 2

# Dostęp do statycznej zmiennej bezpośrednio przez klasę
print(Licznik.licznik_instancji)  # Wynik: 2
