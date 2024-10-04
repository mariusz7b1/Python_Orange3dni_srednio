import os
os.system("cls")


class TestKlasa:
    def __init__(self, wartosc):
        if wartosc % 2 != 0:
            self.a = 1
        else:
            self.b = 1


ob1 = TestKlasa(1)


#  podejscie 1 - mamy bład
print(ob1.a)
# print(ob1.b)  # bład

#  podejscie 2 - obsługujemy błąd

try:
    print(ob1.b)
except AttributeError:
    print("Atrybut b nie istnieje")
    pass


#  podejscie 3 - sprawdzamy czy istanieje
if hasattr(ob1, 'b'):
    print(ob1.b)
else:
    print("brak")
