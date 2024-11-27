"""
Scieżki 
"""
import sys
import site
from os import system
system('cls')
print("scieżki dla modułów")
for p in site.getsitepackages():
    print(p)

print("\n\n")
print("wypisuje ścieżki 'sys.path' to lista")
for p in sys.path:
    print(p)
