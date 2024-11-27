# sortowanie po 2 elemencie tablicy
lst1 = [[4, 2], [3, 1], [1, 7], [5, 6]]


def ts(x):
    return x[1]


print(lst1)

lst2 = sorted(lst1, key=ts)
print(lst2)

lst3 = sorted(lst1, key=lambda x: x[1])
print(lst3)

lst4 = sorted(lst1, key=lambda x: x[0], reverse=True)
print(lst4)
