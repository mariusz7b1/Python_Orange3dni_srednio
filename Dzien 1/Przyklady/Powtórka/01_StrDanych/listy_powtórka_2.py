"""
Listy powtorka cd....
"""
import os
os.system("cls")

lst1 = []
for ele in range(11):
    lst1.append(pow(2, ele))


lst1 = [pow(2, ele) for ele in range(11)]
print(lst1)

print(id(lst1))
lst1 = lst1 + [2048]
print(id(lst1))

print("\nin,  not in")
var1 = 64
if var1 in lst1:
    print(f"wartość {var1} jest na liście i ma index {lst1.index(var1)}")
else:
    print(f"wartość {var1} NIE jest na liście")

for var1 in range(8, 50, 8):
    if var1 not in lst1:
        print(f"wartość {var1} NIE jest na liście")


lst2 = lst1
print(lst1)
print(lst2)
del lst1[1:-1]
print(lst1)
print(lst2)

if id(lst1) == id(lst2):
    print("lst1 i lst2 to dwie różne nazwy tej samej listy ")

lst3 = lst1[:]
print(lst1)
print(lst3)
lst1.clear()
print(lst1)
print(lst3)

if id(lst1) == id(lst3):
    print("lst1 i lst3 to dwie różne nazwy tej samej listy ")
else:
    print("teraz sa rozne")

str1 = "Ala ma kota ale kot nie lubi ali i co z tego"
lst1 = list(str1.lower())
print(f"litera 'a' wystąpiła {lst1.count('a')}")
print(str1.count('b'))
