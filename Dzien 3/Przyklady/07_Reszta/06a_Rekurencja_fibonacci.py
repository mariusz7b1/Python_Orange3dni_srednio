"""
Rekurencja
"""


def fibonacci(n):
    if n <= 0:
        print("Podaj liczbę większą od zera.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


numer_wyrazu = int(
    input("Podaj numer wyrazu ciągu Fibonacciego, który chcesz obliczyć: "))
wynik = fibonacci(numer_wyrazu)
if wynik is not None:
    print(f"{numer_wyrazu}-ty wyraz ciągu Fibonacciego wynosi {wynik}")
