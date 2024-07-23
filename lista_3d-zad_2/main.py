"""Napisz generator, który wczytuje plik tekstowy i zwraca kolejne słowa z pliku,
pomijając znaki interpunkcyjne."""

# skorzystamy z wyrażeń regularnych
#import re
import string  # Import the string module
punctuation = set(string.punctuation)

"""Początkowo wyrażenia regularne, zwłaszcza złożone, mogą się wydawać niezrozumiałym szyfrem, ale z czasem stają się coraz bardziej czytelne. Warto się z nimi zapoznać,,,, ponieważ są potężnym narzędziem, niezwykle przydatnym w pracy z tekstem, danymi czy sekwencjami nukleotydów. Co więcej, składnia i zasady dotyczące wyrażeń regularnych, które tu przedstawię, są podobne w wielu innych językach programowania, programach przeznaczonych do pracy z tekstem (np. grep, sed) czy edytorach tekstu. Zatem opanowanie ich może być przydatne także poza programowaniem w Pythonie."""

def generator(filename):
    with open(filename, 'r') as file:
        # for line in file:
        #     print(f"{line}\n")

        for line in file:
            # Usun znaki inter i podziel wiersz na slowa
            for word in line.strip().split():
                print(all(char in punctuation for char in word))
                if not all(char in punctuation for char in word):
                    # Convert punctuation set to a string for strip
                    yield word.strip(''.join(punctuation))

def generator_collapsible_list(filename):
    with open(filename, 'r') as file:
        result = [word.strip(''.join(punctuation)) for line in file for word in line.strip().split() if not all(char in punctuation for char in word)]
        for word in result:
            yield word

def main():
    print(f"Start...{punctuation}")

    filename = 'words.txt'
    for word in generator(filename):
        print(word)

    print(f"\n fun. generator_collapsible_list()\n")
    for word in generator_collapsible_list(filename):
        print(word)

if __name__ == "__main__":
    main()
