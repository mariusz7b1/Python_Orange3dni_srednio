
"""
+---------------------+
|    Pierwsza_Klasa   |  ← Nazwa klasy
+---------------------+
| wielki_napis: str   |  ← Atrybuty (cechy klasy)
| maly_napis: str     |
+---------------------+
| polacz_napisy()     |  ← Metody (działania klasy)
| powiel_maly_nap(int)|
+---------------------+


"""
from os import system
system('cls')


class Pierwsza_Klasa:
    def __init__(self, napis):     # konstruktor
        print(self)
        self.wielki_napis = napis.upper()
        self.maly_napis = napis.lower()

    def polacz_napisy(self):
        return self.maly_napis+':'+self.wielki_napis

    def powiel_maly_napis(self, ile_razy):
        print(self.maly_napis*ile_razy)

    def powiel_wielki_napis(self, ile_razy):
        print(self.wielki_napis*ile_razy)


obj_1_1 = Pierwsza_Klasa('Ala ma kota')


obj_1_2 = Pierwsza_Klasa('Roman ma Psa')


print(obj_1_1.maly_napis)
print(obj_1_2.wielki_napis)

print(obj_1_1.polacz_napisy())
print(obj_1_2.powiel_maly_napis(12))
print(obj_1_2.powiel_wielki_napis(10))
