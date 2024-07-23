"""Napisz listę składaną, która zwraca listę kwadratów liczb całkowitych z zakresu
od 1 do 10."""

def main():
    print(f"Start...")
    squares = [x**2 for x in range(1, 11)]
    print(squares)


if __name__ == "__main__":
    main()