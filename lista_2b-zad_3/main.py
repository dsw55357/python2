"""Napisz program, który wczytuje plik tekstowy zawierający listę słów (jedno
słowo w każdym wierszu) i zlicza liczbę wystąpień każdego słowa. Obsłuż wyjątki
dla braku pliku, nieprawidłowych danych wejściowych oraz innych błędów podczas
odczytu pliku."""

def main(filename):
    print(f"Start...")
    word_counts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip() # Remove leading/trailing whitespace
                if word: # Check if the line is not empty
                    word_counts[word] = word_counts.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"Successfully read file '{filename}'.")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main("words.txt")