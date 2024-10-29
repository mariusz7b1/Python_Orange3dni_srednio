"""
Testowanie  zmiennych instancji 
"""
from os import system
system("cls")


class TestKlasa:
    def __init__(self, wartosc1=1, wartosc2=2):
        self.__pierwsza = wartosc1
        self.__druga = wartosc2

    def suma_wartosci(self):
        return self.__druga+self.__pierwsza


ob1 = TestKlasa()
ob2 = TestKlasa(2)

# print(ob2.__druga)


ob3 = TestKlasa(4)
# ??
ob3.__trzecia = 5
ob3.czwarta = 10


print(ob1.__dict__)
print(ob2.__dict__)

print(ob3.__dict__)
print(ob3.czwarta)
