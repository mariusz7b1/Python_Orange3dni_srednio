"""
Wymuszanie implementacji metod: Klasa abstrakcyjna służy do definiowania interfejsów, 
wymuszając na klasach dziedziczących zaimplementowanie pewnych metod.
Nie można ich instancjonować: Nie można tworzyć bezpośrednich instancji klasy abstrakcyjnej. 
"""

from abc import ABC, abstractmethod


class Osoba(ABC):

    @abstractmethod
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @abstractmethod
    def get_full_name(self):
        pass


class Pracownicy(Osoba):

    def __init__(self, first, last, salary):
        super().__init__(first, last)
        self.salary = salary

    def get_full_name(self):
        return f'{self.__class__.__name__}: {self.first} {self.last}'


#test = Osoba("mariusz", "nowak")
# Bład

ob1 = Pracownicy("mariusz", "nowak", 3242)
