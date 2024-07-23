"""Napisz program, który wczytuje zdanie od użytkownika i szyfruje je za pomocą
szyfru Cezara, przesuwając każdą literę o podaną liczbę pozycji w alfabecie.
Użyj modułu string do pracy z alfabetem."""

"""Moduł string :
Importowanie: import string
Dostęp do alfabetu: string.ascii_letters
Przesunięcie znaku: (ord(char) - base + shift) % 26 + base"""

import string

def szyfr_cezara(tekst, klucz, decrypt=False):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            shift = klucz if not decrypt else -klucz
            if znak.isupper():
                wynik += chr((ord(znak) - ord('A') + shift) % 26 + ord('A'))
            else:
                wynik += chr((ord(znak) - ord('a') + shift) % 26 + ord('a'))
        else:
            wynik += znak
    return wynik

def main():
    # Wczytuje zdania od użytkownika
    tekst = input("Podaj zdanie do zaszyfrowania: ")

    # Wczytuje liczbę pozycji do przesunięcia
    klucz = int(input("Podaj liczbe pozycji do przesuniecia: "))

    # Szyfrowanie zdania
    szyfrogram = szyfr_cezara(tekst, klucz)

    print("\nZaszyfrowana wiadomosc:\n", szyfrogram)

    wiadomosc = szyfr_cezara(szyfrogram, klucz, True)
    print("\nOdszyfrowana wiadomosc:\n", wiadomosc)

def main_test():
    tekst = "Once the command completes, you will be able to log into the server via SSH without being prompted for a password. However, if you set a passphrase when creating your SSH key, you will be asked to enter the passphrase at that time. This is your local ssh client asking you to decrypt the private key, it is not the remote server asking for a password."
    klucz = 10

    # Szyfrowanie wiadomości
    szyfrogram = szyfr_cezara(tekst, klucz)
    print("\nZaszyfrowana wiadomosc:\n", szyfrogram)

    # Odszyfrowanie wiadomośći
    wiadomosc = szyfr_cezara(szyfrogram, klucz, True)
    print("\nOdszyfrowana wiadomosc:\n", wiadomosc)



if __name__ == "__main__":
    main()
    # main_test()