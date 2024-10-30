from os import system
system("cls")
liczby = list(range(1, 21))
pass

parzyste = list(filter(lambda liczba: liczba % 2 == 0, liczby))
print(parzyste)  # Wynik: [2, 4, 6, 8, 10...]
