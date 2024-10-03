"""Funkcja lucas_sequence jest generatorem,
który zwraca kolejne liczby ciągu Lucasa.
Ciąg Lucasa jest podobny do ciągu Fibonacciego,
z tym że pierwsze dwa elementy są równe 2 i 1
"""


def ciag_lucasa(limit: int):
    """Funkcja zwraca liczby z ciągu Lucasa.

    Args:
        limit (int): maksymalna wartość

    Returns:
        int:  liczby w ciągu Lucasa.
    """
    a, b = 2, 1
    while a <= limit:
        yield a
        a, b = b, a + b


for liczba in ciag_lucasa(1000):
    print(liczba, end=' ')
