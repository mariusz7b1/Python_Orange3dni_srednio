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


def test10(str1):
    print(str1)


ob1.met1 = test10
ob1.met1("to jest napis 1")
ob1.met1("to jest napis 2")
print(ob1.__dict__)
