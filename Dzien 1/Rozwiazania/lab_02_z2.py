import itertools


def check_anagran(t1, t2):
    lst1 = list(t1.replace(" ", "").lower())
    lst2 = list(t2.replace(" ", "").lower())
    lst1.sort()
    lst2.sort()
    return True if (lst1 == lst2) else False


lst_text = ['optyczny', 'poczytny', 'chityna', 'hiacynt', 'alergia', 'galeria']
kombinacje = list(itertools.combinations(lst_text, 2))
for kombinacja in kombinacje:
    print(f"Czy {kombinacja} jest anagramem ? ", end="")
    print(check_anagran(kombinacja[0], kombinacja[1]))
