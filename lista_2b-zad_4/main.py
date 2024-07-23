"""Stwórz funkcję, która prosi użytkownika o wprowadzenie adresu URL, a następnie
próbuje pobrać zawartość strony. Jeśli strona nie istnieje lub wystąpi inny
błąd, obsłuż odpowiednie wyjątki (np. URLError , HTTPError ) i poproś
użytkownika o wprowadzenie adresu URL ponownie. Funkcja powinna zwracać
zawartość strony."""

#import requests
# python -m pip install requests
#from bs4 import BeautifulSoup
# pip install beautifulsoup4
# pip install -r requirements.txt

import urllib.request
from urllib.error import URLError, HTTPError

def main():
    print(f"Start...")

    try:
        url = input("Wprowadz adres URL: ")
        #url = "https://ambrogio.pl/"
        response = urllib.request.urlopen(url)
        page_content = response.read().decode('utf-8')
        print(page_content)
        #break
    except HTTPError as e:
        print(f"HTTP error occurred: {e.code} {e.reason}")
        print("Please enter a valid URL.")
    except URLError as e:
        print(f"URL error occurred: {e.reason}")
        print("Please enter a valid URL.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please enter a valid URL.")

if __name__ == "__main__":
    main()


# HTTPError: Catches HTTP errors, such as 404 (Not Found) or 403 (Forbidden).
# URLError: Catches errors related to the URL itself, such as when the domain does not exist.
# Exception: Catches any other unexpected exceptions.
# https://realpython.com/urllib-request/