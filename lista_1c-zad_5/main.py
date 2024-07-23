"""Stwórz moduł wyszukiwanie_tekstowe.py , który zawiera funkcje do wyszukiwania
wzorców w tekście (np. wyszukiwanie za pomocą algorytmu Knutha-Morrisa-Pratta,
algorytmu Boyera-Moorea, wyrażeń regularnych). Zaimportuj ten moduł do innego
programu i użyj go do wyszukiwania wzorców w przykładowych tekstach."""

import wyszukiwanie_tekstowe

def main():
    #
    #
    # 5. Wyszukiwanie wzorców w tekście
    # 5.1 wyszukiwanie za pomocą algorytmu Knutha-Morrisa-Pratta
    # przykład użycia

    print("\n5. Wyszukiwanie wzorcow w tekscie\n")
    text = "The new line character in Python is n. It is used to indicate the end of a line of text"
    pattern = "line"
    #print("\n tekst: {} \n wzorzec: {}\n".format(text, pattern))
    matches = wyszukiwanie_tekstowe.kmp_search(text, pattern)

    text = "The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match. "
    pattern = "know"
    matches = wyszukiwanie_tekstowe.kmp_search(text, pattern)

if __name__ == "__main__":
    main()