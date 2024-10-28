"""
Funkcje zew wew
"""
from os import system
system('cls')


def funkcja_zew(a: int, b: int) -> None:

    def funkc_wew():
        print(f"Welcome a={a} b={b}")

    print("Funkcja zewnetrzna")
    funkc_wew()
    print("cos sie dzieje")
    a, b = b, a
    funkc_wew()


funkcja_zew(100, 200)
