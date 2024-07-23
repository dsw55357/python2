"""3. Napisz listę składaną, która tworzy listę liczb parzystych z zakresu od 1 do
20."""

def main():
    print(f"Start...")
    listp = [x for x in range(1, 21) if x % 2 == 0]
    print(listp)

if __name__ == "__main__":
    main()