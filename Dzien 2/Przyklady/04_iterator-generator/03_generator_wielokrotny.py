def moj_generator(war_maks):
    war = 1
    while war <= war_maks:
        yield war
        war += 1


for i in moj_generator(3):
    print(i)

pass
# zastanowaic sie jaki bedzie wynik dzialania
# co pojawi się na ekranie , ewentualnie ile razy wykona się print()
for i in moj_generator(5):
    for j in moj_generator(2):
        print(i * j, sep=' ')


# pozniej to

print('#' * 25)

a = moj_generator(5)
b = moj_generator(2)
for i in a:
    for j in b:
        print(i * j, sep=' ')
