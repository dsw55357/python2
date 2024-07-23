"""Napisz program, który wczytuje dane od użytkownika i próbuje przekształcić je
na datę (format: RRRR-MM-DD ). Obsłuż wyjątki dla nieprawidłowych danych
wejściowych oraz niepoprawnych wartości dla roku, miesiąca i dnia."""

from datetime import datetime

def main():
    print(f"Start...")
    while True:
        try:
            date_string = input("Podaj prosze date w formacie YYYY-MM-DD: ")
            date_object = datetime.strptime(date_string, "%Y-%m-%d")
            print(f"Data {date_object}")
            return date_object
        except ValueError as e:
            print(f"Nieprawidlowy format daty: {e}. Prosze wprowadz date raz jeszcze.")

if __name__ == "__main__":
    main()