"""
Przykłądowe rozwiąznie zadania 3 z listy 4
"""
from os import system
system("cls")


def polacz_listy(list1, list2):
    list1_iter = iter(list1)
    list2_iter = iter(list2)

    while True:  # działamy aż do wystąpienia błedu tj. wyczerpanie jednej z list
        try:
            yield next(list1_iter)
        except StopIteration:
            break

        try:
            yield next(list2_iter)
        except StopIteration:
            break

    # jeśli jedna jest dluższa kontynuuejemy
    for item in list1_iter:
        yield item
    for item in list2_iter:
        yield item


lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd', 'e', 'f']

for war in polacz_listy(lst1, lst2):
    print(war, end="-")
