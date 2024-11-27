"""
comprehension
"""
# Lista
list_comprehension = [x**2 for x in range(10)]

# Lista  z warunkiem
# Tworzenie listy kwadratów tylko dla liczb parzystych
list_comprehension_with_condition = [x**2 for x in range(10) if x % 2 == 0]

# zbiór
# Tworzenie zbioru liczb podzielnych przez 3 z zakresu 0-19
set_comprehension = {x for x in range(20) if x % 3 == 0}

# słownik
# Tworzenie słownika, gdzie klucz to liczba, a wartość to jej kwadrat
dict_comprehension = {x: x**2 for x in range(5)}

# Złożona lista
# Tworzenie listy par (x, y), gdzie x i y są liczbami od 0 do 2
nested_comprehension = [(x, y) for x in range(3) for y in range(3)]
