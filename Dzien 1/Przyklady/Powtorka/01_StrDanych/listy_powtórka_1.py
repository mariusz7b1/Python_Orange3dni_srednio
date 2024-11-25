""""
Listy powtórka 1
"""
import os
os.system("cls")

# Podstawa
lst1 = [1, 32, 3, 4]
lst2 = ["ala", "ma"]
lst3 = [56.3, -19.1]

lst1 = lst1+lst2
lst1.extend(lst3)
lst1 += [(1, 2)]

print(lst1)
print(type(lst1))
print("ilość elementów ", len(lst1))

print(lst1[3])
print(lst1[-1][1])


# modyfikacje listy
del lst1[1]
print(lst1.pop(-1))


print(lst1)

lst1.append(13)
lst1.insert(2, 2)
lst1.insert(17, 14)     # ??
print(lst1)

print("\nslice (Wycinki)")


lst1_wycinek1 = lst1[4:6]
lst1_wycinek2 = lst1[4:-2]
lst1_wycinek3 = lst1[:-2]
lst1_wycinek4 = lst1[-1:]
print(lst1_wycinek1)
print(lst1_wycinek2)
print(lst1_wycinek3)
print(lst1_wycinek4)

del lst1[4:6]
print(lst1)

lst1.sort()
print(lst1)
print(sorted(lst1, reverse=True))
print(lst1)
lst1.insert(4, 1000)
lst1.reverse()
print(lst1)

# wycinanie z krokiem
lst1_wycinek1 = lst1[1:5:2]
lst1_wycinek2 = lst1[::3]
lst1_wycinek3 = lst1[::-1]    # ciekawe wykorzystannie
lst1_wycinek4 = lst1[::-2]

print(lst1_wycinek1)
print(lst1_wycinek2)
print(lst1_wycinek3)
print(lst1_wycinek4)
