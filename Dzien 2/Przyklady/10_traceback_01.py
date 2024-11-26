"""
Obsługa błędów z wyświetleniem traceback
"""
from os import system
from sys import exc_info
import traceback
system('cls')
try:
    # Kod, który może wygenerować wyjątek
    licznik = 10 / 0
except Exception as e:
    print("Wystąpił błąd!")
    traceback.print_exc()  # Wyświetla pełny traceback błędu

# Zapis traceback do zmiennej:
try:
    licznik = 10 / 0
except Exception as e:
    blad = traceback.format_exc()  # Pobiera traceback jako string
    print(f"Traceback zapisany w zmiennej:\n{blad}")

# Przykład z użyciem extract_tb:
try:
    wynik = 10 / 0
except Exception as e:
    tb = traceback.extract_tb(e.__traceback__)
    for frame in tb:
        print(f"Plik: {frame.filename}, Linia: {
              frame.lineno}, Kod: {frame.line}")

# Przykład z użyciem exc_info:
try:
    licznik = 10 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = exc_info()
    print(f"Typ wyjątku: {exc_type}")
    print(f"Wartość wyjątku: {exc_value}")
