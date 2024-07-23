"""Napisz listę składaną, która tworzy listę wszystkich liter w podanym tekście,
ignorując spacje i znaki interpunkcyjne."""

import string  # Import the string module
punctuation = set(string.punctuation)

"""Początkowo wyrażenia regularne, zwłaszcza złożone, mogą się wydawać niezrozumiałym szyfrem, ale z czasem stają się coraz bardziej czytelne. Warto się z nimi zapoznać,,,, ponieważ są potężnym narzędziem, niezwykle przydatnym w pracy z tekstem, danymi czy sekwencjami nukleotydów. Co więcej, składnia i zasady dotyczące wyrażeń regularnych, które tu przedstawię, są podobne w wielu innych językach programowania, programach przeznaczonych do pracy z tekstem (np. grep, sed) czy edytorach tekstu. Zatem opanowanie ich może być przydatne także poza programowaniem w Pythonie."""

def collapsible_list(filename):
    with open(filename, 'r') as file:
        # result = [word.strip(''.join(punctuation)) for line in file for word in line.strip().split() if not all(char in punctuation for char in word)]
        # print(result)
        result = [char for line in file for word in line.strip().split() if not all(char in punctuation for char in word) for char in word.strip(''.join(punctuation))]
        print(result)

        # for word in result:
        #print(result)

def main():
    print(f"Start...")

    filename = 'words.txt'
    collapsible_list(filename)

if __name__ == "__main__":
    main()