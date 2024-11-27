class Osoba():

    def __init__(self, imie, ile_lat):
        self.__imie = imie
        self.__wiek = ile_lat

    @property        # odczytaj __wiek
    def wiek(self):
        return self.__wiek

    @wiek.setter    # ustaw __wiek
    def wiek(self, wartosc):
        if wartosc < 0:
            raise ValueError("Wiek nie może być ujemny.")
        self.__wiek = wartosc

    @wiek.deleter   # usun __wiek
    def wiek(self):
        self.__wiek = 0

    @property        # odczytaj __imie
    def imie(self):
        return self.__imie

    @imie.setter    # ustaw __imie
    def imie(self, wartosc):
        if wartosc is None:
            raise ValueError("Imie nie może być puste.")
        elif not wartosc.isalpha():
            raise ValueError(
                "Imie nie może zawierać nieprawidłowych znaków.")
        self.__imie = wartosc


pracownik1 = Osoba("Anna", 30)
pracownik2 = Osoba("Marcin", 40)
print(pracownik1.wiek)  # Wynik: 30
print(pracownik2.wiek)  # Wynik: 40

# minelo 10 lat:)
pracownik1.wiek = 40
pracownik2.wiek = 50

del pracownik1.wiek

# ma byc miło
pracownik1.imie = "Anusia"
pracownik2.imie = "Marcinek"

print(f"{pracownik1.imie} ma {pracownik1.wiek} lat.")
print(f"{pracownik2.imie} ma {pracownik2.wiek} lat.")
