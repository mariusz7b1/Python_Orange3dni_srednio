"""
Przykladowy moduł 
"""
import itertools

imiona = ['Anna', 'Jan', 'Karolina']
nazwiska = ['Kowalski', 'Nowak', 'Szymański']
wiek = list(range(100))

kombinacje = list(itertools.product(imiona, nazwiska, wiek))

print(f"Ilość kombinacji wynosi {len(kombinacje)}")

# print(kombinacje)
