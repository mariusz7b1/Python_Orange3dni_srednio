"""
Przykład uzycia  Defaultdict 
ułatwia pracę z wartościami domyślnymi

"""
from collections import defaultdict

# Przykładowe zdania
zdania = [
    "Ala ma kota",
    "Ala ma psa",
    "Ola ma psa i kota"
]

# Tworzymy defaultdict, gdzie każde nowe słowo ma domyślną wartość 0
licznik_slow = defaultdict(lambda: 0)

# Dla każdego zdania z listy
for zdanie in zdania:
    # Dla każdego słowa w zdaniu (podzielone przez spacje)
    for slowo in zdanie.split():
        licznik_slow[slowo] += 1

# Wynik
for slowo, liczba in licznik_slow.items():
    print(f"Słowo '{slowo}' występuje {liczba} razy.")
