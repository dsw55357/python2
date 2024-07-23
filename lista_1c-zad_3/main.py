"""Stwórz moduł liczby_zespolone.py zawierający funkcje do dodawania,
odejmowania, mnożenia i dzielenia liczb zespolonych. Zaimportuj moduł do innego
programu i użyj go, aby obliczyć wynik operacji na liczbach zespolonych."""

"""Zmodyfikuj moduł liczby_zespolone.py , dodając obsługę wyjątków, aby uniknąć
błędów podczas dzielenia przez zero oraz podawania nieprawidłowych argumentów."""

#
#
# 1 + 3. Liczby zespolone
def main():
    from liczby_zespolone import tComplex
    lz_ = tComplex(5+2j, 0)
    # Dodawanie
    lz_.add()
    # Odejmowanie
    lz_.sub()
    # Mnożenie
    lz_.mul()
    # Dzielenie
    lz_.div()


if __name__ == "__main__":
    main()