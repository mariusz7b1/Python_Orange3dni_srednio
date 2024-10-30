
"""
Przykładowe rozwiązanie zadania 7 z listy 5
Nie przewiduje się powtarzajacych się nazwisk, należy rozbudować kod o taką
możliwość wprowadzajac np dodatkowe unikatowe pole w sposob jednoznaczny
"""
from os import system
system("cls")


class Firma:
    __stanowiska = ["CEO", "CTO", "CFO", "Manager", "Developer", "HR"]

    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
        self.pracownicy = []

    def dodaj_pracownika(self, nazwisko, stanowisko):
        if stanowisko in self.__stanowiska:
            self.pracownicy.append(
                {"nazwisko": nazwisko, "stanowisko": stanowisko})
        else:
            print("Niedozwolone stanowisko. Wybierz jedno z dopuszczalnych! ")

    def usun_pracownika(self, nazwisko):
        for pracownik in self.pracownicy:
            if pracownik["nazwisko"] == nazwisko:
                self.pracownicy.remove(pracownik)
                break

    def zmien_stanowisko(self, nazwisko, nowe_stanowisko):
        if nowe_stanowisko in self.__stanowiska:
            for pracownik in self.pracownicy:
                if pracownik["nazwisko"] == nazwisko:
                    pracownik["stanowisko"] = nowe_stanowisko
        else:
            print("Niedozwolone stanowisko. Wybierz jedno z dopuszczalnych !")


firma = Firma("Example Corp.", "ul. Przykładowa 1")
firma.dodaj_pracownika("Kowalski", "CEO")
firma.dodaj_pracownika("Nowak", "Developer")
print(firma.pracownicy)

firma.usun_pracownika("Kowalski")
firma.usun_pracownika("Kowal")
print(firma.pracownicy)

firma.zmien_stanowisko("Nowak", "HR")
print(firma.pracownicy)
