from os import system
system("cls")

lst1 = list(range(1, 11, 2))
print(lst1)

lst1 = enumerate(lst1)
print(lst1, type(lst1))

lst1 = list(enumerate(lst1))
print(lst1, type(lst1))

for pos, value in lst1:
    print('indeks:', pos, 'wartosc', value)

lst2 = ['I', 'III', 'V', 'VII', 'IX']

zip_lst = list(zip(lst1, lst2))
print(zip_lst, type(zip_lst))

for l_arab, l_rzym in zip_lst:
    print('Liczba arabska', l_arab, 'to rzymskie', l_rzym)


for pos, (l_arab, l_rzym) in enumerate(zip(lst1, lst2)):
    print(pos, l_arab, l_rzym)
