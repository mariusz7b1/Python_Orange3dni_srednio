class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def jedz(self):
        print(f"{self.marka} {self.model} jedzie.")


class SportowySamochod(Samochod):
    def __init__(self, marka, model, moc):
        super().__init__(marka, model)
        self.moc = moc

    def jedz(self):
        print(f"{self.marka} {self.model} jedzie z mocą {self.moc} KM.")


bmw = SportowySamochod("BMW", "M3", 450)
bmw.jedz()  # wyświetli "BMW M3 jedzie z mocą 450 KM."
