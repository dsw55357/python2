"""Stwórz moduł wyszukiwanie_tekstowe.py , który zawiera funkcje do wyszukiwania
wzorców w tekście (np. wyszukiwanie za pomocą algorytmu Knutha-Morrisa-Pratta,
algorytmu Boyera-Moorea, wyrażeń regularnych). Zaimportuj ten moduł do innego
programu i użyj go do wyszukiwania wzorców w przykładowych tekstach."""

def kmp_table(pattern):
    """
    Oblicza tablicę prefikso-sufiksów dla danego wzorca.

    Argumenty:
    pattern: Ciąg znaków, który jest wzorem.

    Zwraca:
    Tablica prefikso-sufiksów dla danego wzorca.
    """
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def preprocess_text(text):

    """
    Removes newline characters from the text.
    """
    return text.replace("\n", "")

def kmp_search(text, pattern):
    """
    Wyszukiwuje wszystkie wystąpienia wzorca w tekście za pomocą algorytmu Knutha-Morrisa-Pratta.

    Argumenty:
    text: Ciąg znaków, w którym szukamy wzorca.
    pattern: Ciąg znaków, który jest wzorem.

    Zwraca:
    Lista indeksów, gdzie zaczynają się kolejne wystąpienia wzorca w tekście.
    """
    # text = preprocess_text(text)
    # text = text.lower()  # Convert text to lowercase for case-insensitive search
    # pattern = pattern.lower()  # Convert pattern to lowercase for case-insensitive search

    pi = kmp_table(pattern)
    #print("{} \n".format(pi))
    i = 0
    j = 0
    occurrences = 0
    matches = []
    while i < len(text):
        # if j > 0 and text[i] != pattern[j]:
        while j > 0 and j < len(pattern) and text[i] != pattern[j]:
        #     print(f"# i={i}, j={j}")
            j = pi[j - 1]

        if j < len(pattern) and text[i] == pattern[j]: # Check if j is within bounds
            j += 1

        if j == len(pattern):
            print(f"Pattern found at index {i - len(pattern) + 1}")
            matches.append(i - len(pattern) + 1)
            j = pi[j - 1]
            #break
            #j=0
        i += 1

    print("Znaleziono wystapien: {}\nwzorca: '{}'\nw tekscie: '{}'".format(len(matches), pattern, text))
    for match in matches:
        print(f"  - indeks {match}")
    print("\n")

    return matches