"""Napisz program, który wczytuje dwie macierze od użytkownika i wykonuje operacje
matematyczne (dodawanie, odejmowanie, mnożenie) na tych macierzach. Obsłuż
wyjątki dla nieprawidłowych danych wejściowych oraz niekompatybilnych rozmiarów
macierzy."""


def read_matrix(message):
    print(message)
    rows = int(input("Wprowadz ilosc wierszy: "))
    cols = int(input("Wprowadz ilosc kolumn: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Uzypelnij wiersz {i+1} wartosc: ").split()))
        if len(row) != cols:
            raise ValueError("Niespojna liczba kolumn w macierzy.")
        matrix.append(row)
    return matrix

def add_matrices(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Aby można było dodać, macierze muszą mieć te same wymiary.")
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def subtract_matrices(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Aby moc odejmowac, macierze musza miec te same wymiary.")
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def multiply_matrices(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("Aby mozliwe bylo pomnozenie, liczba kolumn pierwszej macierzy musi byc rowna liczbie wierszy drugiej macierzy.")
    result = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*m2)] for X_row in m1]
    return result

def main():
    try:
        print(">> Dodawanie macierzy:")
        m1 = read_matrix("* Podaj pierwsza macierz:")
        m2 = read_matrix("* Podaj druga macierz:")
        print(add_matrices(m1, m2))

        print(">> Odejmowanie macierzy:")
        m1 = read_matrix("* Podaj pierwsza macierz:")
        m2 = read_matrix("* Podaj druga macierz:")
        print(subtract_matrices(m1, m2))

        print(">> Mnozenie macierzy:")
        m1 = read_matrix("* Podaj pierwsza macierz:")
        m2 = read_matrix("* Podaj druga macierz:")
        print(multiply_matrices(m1, m2))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
