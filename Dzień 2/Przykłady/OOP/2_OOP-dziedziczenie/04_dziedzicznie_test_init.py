# Przykład z dziedziczeniem wielokrotnym:
class Pojazd:
    def __init__(self,):
        print("Wywołanie w Pojazd", self.__class__.__name__)

    def jedz(self):
        print("Pojazd jedzie")


class Samochod(Pojazd):
    def __init__(self):
        print("Wywołanie w Samochod", self.__class__.__name__)

    def jedz(self):
        print("Samochod jedzie ")


class SportowySamochod(Samochod):
    # def __init__(self):
    #    print("Wywołanie w SportowySamochod", self.__class__.__name__)
    def jedz(self):
        print(" Sportowy samochod jedzie ")


pass
bmw = SportowySamochod()
bmw.jedz()
