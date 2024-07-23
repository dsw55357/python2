"""Napisz program, który generuje i wypisuje 10 losowych liczb z zakresu od 1 do
100, korzystając z modułu random ."""

""" Moduł random:
Importowanie: import random
Generowanie losowej liczby: random.randint(min, max)"""

from random import randint

def main():
    for _ in range(10):
        print(randint(1, 100))

if __name__ == "__main__":
    main()