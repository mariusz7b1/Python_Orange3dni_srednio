""" implementacja ppopularnej w latach 70-80 :) gry pomidor
    w erze przed smartfonowej
"""
from os import system
system('cls')

MAGICZNE_SLOWO = 'pomidor'

slowo = MAGICZNE_SLOWO
while slowo == MAGICZNE_SLOWO:
    slowo = input('podaj slowo: ')

print("Skonczyłeś grać w pierwsza cześć gry ")
print("*"*20)

while True:
    slowo = input('podaj slowo: ')
    if slowo != MAGICZNE_SLOWO:
        break

print("Skonczyłeś grać w drugą cześć gry ")
print("*"*20)
