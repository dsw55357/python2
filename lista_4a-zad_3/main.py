"""Stwórz program, który wczytuje plik tekstowy i zapisuje jego zawartość w
odwrotnej kolejności do nowego pliku. Użyj modułu os do manipulacji plikami
oraz ścieżkami."""

""" Moduł os:
Importowanie: import os
Odczyt i zapis do pliku: open(file_path, mode)
Zamknięcie pliku: file.close()"""

import os

def main():
    # Open the source file and read its contents
    with open("source.txt", "r") as source:
        data = source.read()

    source.close()

    # Reverse the order of the characters in the data
    reversed_data = data[::-1]

    # Open a new file in write mode and write the reversed data to it
    with open("target.txt", "w") as target:
        target.write(reversed_data)

    target.close()


if __name__ == "__main__":
    main()