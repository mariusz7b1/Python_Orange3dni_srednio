class Samochod:
    liczba_samochodow = 0  # Atrybut klasowy (wspólny dla wszystkich instancji)

    def __init__(self, marka, model, rok):
        self.marka = marka  # Atrybut instancji (właściwość konkretnej instancji)
        self.model = model
        self.rok = rok
        Samochod.liczba_samochodow += 1  # Zwiększanie liczby samochodów przy każdej nowej instancji

    # Metoda instancji (operuje na danych konkretnego obiektu)
    def info(self):
        return f"Samochód: {self.marka} {self.model}, Rok: {self.rok}"

    # Metoda klasowa (operuje na klasie, nie na instancji)
    @classmethod
    def ile_samochodow(cls):
        return f"Łączna liczba samochodów: {cls.liczba_samochodow}"

    # Metoda statyczna (nie ma dostępu ani do instancji, ani do klasy, działa jak zwykła funkcja)
    @staticmethod
    def sprawdz_vin(vin):
        # Zakładamy, że poprawny numer VIN ma 17 znaków
        return len(vin) == 17

# Przykład użycia klasy

# Tworzenie instancji klasy Samochod (wywołanie metody instancji)
samochod1 = Samochod("Toyota", "Corolla", 2020)
samochod2 = Samochod("Tesla", "Model 3", 2021)

# Wywołanie metody instancji
print(samochod1.info())  # Samochód: Toyota Corolla, Rok: 2020
print(samochod2.info())  # Samochód: Tesla Model 3, Rok: 2021

# Wywołanie metody klasowej (na klasie)
print(Samochod.ile_samochodow())  # Łączna liczba samochodów: 2

# Wywołanie metody statycznej (sprawdza, czy VIN jest poprawny)
print(Samochod.sprawdz_vin("1HGCM82633A123456"))  # True
print(Samochod.sprawdz_vin("123456"))  # False
