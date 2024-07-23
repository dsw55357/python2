"""Napisz funkcję, która wczytuje liczbę od użytkownika i oblicza jej silnię.
Obsłuż wyjątki dla ujemnych wartości oraz nieprawidłowych danych wejściowych."""

def main():

    count = 3 # Maximum number of attempts allowed
    while count > 0:
        try:
            number = int(input("Podaj liczbe do obliczenia silni: "))
            if number < 0:
                print("Liczby ujemne nie nadaja sie do obliczen silni")
                count -= 1
            else:
                factorial = 1
                for i in range(1, number + 1):
                    factorial *= i
                print(f"Silnia z liczby {number} wynik {factorial}.")
                break # Exit the loop if the calculation is successful
        except ValueError:
            print("Nieprawidlowe dane wejsciowe. Wprowadz prawidłowa liczbe calkowita.")
            count -= 1
        if count == 0:
            print("No more attempts. Exiting.")
            break

if __name__ == "__main__":
    #n = 1 n! = 1
    #n = 2 n! = 2
    #n = 3 n! = 6
    #n = 4 n! = 24
    #n = 5 n! = 120
    #n = 6 n! = 720
    #n = 7 n! = 5040
    #n = 8 n! = 40320
    #n = 9 n! = 362880
    #n = 10 n! = 3628800
    #n = 11 n! = 39916800
    #n = 12 n! = 479001600
    main()