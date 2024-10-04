from os import system
system("cls")

owoce = ['jabłko', 'banan', 'pomarańcza']

for owoc in enumerate(owoce):
    # print(type(owoc))
    print(owoc)


slowo = 'hello'
for char in enumerate(slowo):
    print(char)

for indeks, owoc in enumerate(owoce):
    print(indeks, owoc)
