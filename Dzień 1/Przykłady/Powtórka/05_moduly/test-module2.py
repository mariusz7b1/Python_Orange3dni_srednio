# Test modułów 2 + pomiar czasu
import mpmodul_2
import datetime
from random import randint
from os import system


system("cls")

print(f"Ilość wywołań funkcji z moduły wynosi {mpmodul_2.__licznik}")

lst = [randint(0, 10) for i in range(1000000)]   #


# test 1 - unique  z wykorzystaniem set
start = datetime.datetime.now()
lst_wynik = mpmodul_2.unique_list(lst)
duration = datetime.datetime.now() - start

print(lst_wynik)
print(f"czas wykonania: wynosi {duration.microseconds:,} mikrosekund")


# test 2 - unique tradycyjne
start = datetime.datetime.now()
lst_wynik = mpmodul_2.unique_list_2(lst)
duration = datetime.datetime.now() - start

print(lst_wynik)
print(f"czas wykonania: wynosi {duration.microseconds:,} mikrosekund")
pass
# test 3 suma tradycyjna
start = datetime.datetime.now()
suma = mpmodul_2.sum_lst(lst)

duration = datetime.datetime.now() - start
print(
    f"suma wynosi {suma} a czas wykonania wynosi:{duration.microseconds:,} mikrosekund")

# test 4 suma wbudowana
start = datetime.datetime.now()
suma = sum(lst)
duration = datetime.datetime.now() - start
print(
    f"suma wynosi {suma} a czas wykonania wynosi:{duration.microseconds:,} mikrosekund")

print(f"Ilość wywołań funkcji z moduły wynosi {mpmodul_2.__licznik}")
