"""Napisz program, który wczytuje listę słów z pliku tekstowego i wypisuje 5
najczęściej występujących słów oraz ich liczbę wystąpień. Użyj modułu
collections ."""

"""Moduł collections :
Importowanie: from collections import Counter
Zliczanie wystąpień elementów: Counter(iterable).most_common(n)"""

import os
from collections import Counter

def main():
    # Otwiera plik źródłowy, zaczytuje jego zawartość
    with open("source.txt", "r", encoding='utf-8') as source:
        data = source.read().split()

    source.close()

    # Zlicza wystąpienia słów
    licznik = Counter(data)

    # Wypisuje 5 najczęściej występujących słów oraz ich liczby wystąpień
    najczestsze_slowa = licznik.most_common(5)
    for slowo, liczba in najczestsze_slowa:
        print("Slowo: {}, Liczba wystapien: {}".format(slowo, liczba))


if __name__ == "__main__":
    main()