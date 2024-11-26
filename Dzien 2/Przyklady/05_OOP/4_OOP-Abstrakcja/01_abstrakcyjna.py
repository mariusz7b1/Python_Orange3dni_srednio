"""
by stworzyć klasę abstrakcyjną, w Pythonie korzystamy z następujących elementów:
Import modułu abc:

Dziedziczenie po ABC:
Klasa, która ma być abstrakcyjna, musi dziedziczyć po klasie ABC.

Dekorator @abstractmethod:
Metody, które mają być abstrakcyjne (czyli muszą zostać zaimplementowane przez klasy pochodne), 
są oznaczane za pomocą dekoratora @abstractmethod.
"""

from abc import ABC, abstractmethod


class Figura(ABC):   # moja klasa abstr.

    @abstractmethod
    def oblicz_pole(self):
        pass

    @abstractmethod
    def oblicz_obwod(self):
        pass


class Kwadrat(Figura):

    def __init__(self, bok):
        self.bok = bok
    
    def oblicz_pole(self):
        return self.bok * self.bok
    

    def oblicz_obwod(self):
        return self.bok * 4


class Prostokat(Figura):

    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2

    def oblicz_pole(self):
        return self.bok1 * self.bok2

    def oblicz_obwod(self):
        return self.bok1 * 2+self.bok2 * 2


kwadrat = Kwadrat(4)
print(kwadrat.oblicz_pole())  # Wynik: 16

prostokat = Prostokat(4, 5)
print(prostokat.oblicz_obwod())
