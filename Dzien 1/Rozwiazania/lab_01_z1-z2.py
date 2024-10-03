"""
Przykładowa Relizacja zadania z listy 02b zadanie 1 i 2
"""
from os import system
system('cls')


OD = 1
DO = 200
while True:
    ilosc_blokow = input(f"Wprowadź liczbę bloków od {OD} do {DO}: ")
    if ilosc_blokow.isdigit():
        ilosc_blokow = int(ilosc_blokow)
        if ilosc_blokow >= OD and ilosc_blokow <= DO:
            break
        else:
            print(f"Liczba poza zakresem ma być {OD} do {DO} !!!")
    else:
        print("PODAJ LICZBĘ  naturalną !!!")

wysokosc = 0
blokow_na_pietro = 1
wykorzystane_bloki = 0
while ilosc_blokow > 0:
    wysokosc += 1
    wykorzystane_bloki += blokow_na_pietro
    ilosc_blokow -= blokow_na_pietro
    blokow_na_pietro += 1
    if blokow_na_pietro > ilosc_blokow:
        break

print("Wysokość piramidy wynosi:", wysokosc)

spac = (wysokosc) // 2 + wysokosc
for i in range(1, wysokosc+1):
    print(" "*spac, end="")
    print('* '*i)
    spac -= 1

print(f"Wykorzystano {wykorzystane_bloki}",
      f"pozostało {ilosc_blokow} bloków")
input()
