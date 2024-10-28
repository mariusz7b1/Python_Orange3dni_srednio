# list 2 wymiary
lst1 = [[str(j)+":"+str(i) for i in range(4)] for j in range(3)]

for i in lst1:
    print(i)

# wyrażenie listowe
lst1 = [[[str(x)+"-"+str(y)+"-"+str(z) for z in range(4)]
         for y in range(4)] for x in range(4)]

# tradycyjnie listowe
lst2 = []
for x in range(4):
    lst2.append([])
    for y in range(4):
        lst2[x].append([])
        for z in range(4):
            lst2[x][y].append(str(x)+"-"+str(y)+"-"+str(z))

print(lst1[3][1][2])
print(lst2[3][1][2])
