
lista1 = ['jeden', 'dwa', 'trzy']
lista2 = [1, 2, 3, 4, 5]

sparowane_elementy = zip(lista1, lista2)
print(type(sparowane_elementy))
print(list(sparowane_elementy))

for element1, element2 in sparowane_elementy:
    print(f'{element1}: {element2}')

print("\n\n")
sparowane_elementy = zip(lista1, lista2)
for element in sparowane_elementy:
    print(f'{element[0]}: {element[1]}')
