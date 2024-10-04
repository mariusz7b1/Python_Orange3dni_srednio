from os import system
system("cls")


tekst = "Ala ma kota i co z tego skoro kot nie lubi Ali ale też ala nie lubi"
litery = list((tekst.lower()).replace(" ", ""))

# print(litery)
# a zwraca True gdy samogloska


def filtruj_samogloski(litera):
    samogloski = ['a', 'ą', 'e', 'ę' 'i', 'o', 'u', 'ó', 'y']
    return True if litera in samogloski else False


# tu filtrowanie reszta to dadosna twórczość
same_samogloski = filter(filtruj_samogloski, litery)

# nowy tekst to same samogłoski
nowy_tekst = "".join(list(same_samogloski))
print(nowy_tekst)
