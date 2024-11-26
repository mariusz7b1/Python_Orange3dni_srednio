class TestKlasa:
    def sprawdz_atrybut(self):
        # Próba dostępu do dynamicznie dodanego atrybutu
        if hasattr(self, 'testowy'):
            return f"Atrybut testowy istnieje i ma wartość {self.testowy}"
        else:
            return "Atrybut testowy nie istnieje w tej instancji"


# Tworzenie instancji
ob1 = TestKlasa()
ob2 = TestKlasa()

# Dynamiczne dodanie atrybutu
ob1.testowy = 10

# Wywołanie metody
# Wyświetli: Atrybut testowy istnieje i ma wartość 10
print(ob1.sprawdz_atrybut())
# Wyświetli: Atrybut testowy nie istnieje w tej instancji
print(ob2.sprawdz_atrybut())
