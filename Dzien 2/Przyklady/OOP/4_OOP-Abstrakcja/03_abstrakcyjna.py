"""
Klasy abstrakcyjne mogą mieć implementowane metody:
Nie wszystkie metody muszą być abstrakcyjne. 
Klasa abstrakcyjna może zawierać metody z pełną implementacją, 
które klasy pochodne mogą dziedziczyć i używać bez modyfikacji.
"""

from abc import ABC, abstractmethod


class Pojazd(ABC):

    @abstractmethod
    def uruchom_silnik(self):
        pass

    def info(self):  # Metoda z pełną implementacją
        print("To jest pojazd.")


class Samochod(Pojazd):

    def uruchom_silnik(self):
        print("Uruchamianie silnika samochodu.")


# Tworzenie instancji klasy pochodnej
samochod = Samochod()
samochod.uruchom_silnik()  # Wywołuje metodę zaimplementowaną w klasie Samochod
samochod.info()  # Wywołuje metodę z klasy Pojazd (odziedziczoną)
