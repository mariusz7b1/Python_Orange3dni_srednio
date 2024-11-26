class MyString(str):
    def __init__(self, text) -> None:
        super().__init__()
        self.dlugosc = len(text)

    def reverse(self):
        return self[::-1]

    def myenumer(self):
        return list(enumerate(self))

    def my_split(self):
        return "A"


mystr1 = MyString("Ala ma kota")

print(mystr1.reverse())     # moja metoda
print(mystr1)

print(mystr1.split())       # metoda oryg
print(mystr1.dlugosc)
print(mystr1.upper())
print(mystr1.myenumer())
