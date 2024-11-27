"""Test modułow 1"""
from os import system
import mpmodul_2 as rd

system('cls')

wiek = rd.read_int("podaj swoj wiek", 18, 99)
print(wiek)
