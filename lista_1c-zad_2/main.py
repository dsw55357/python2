"""Stwórz moduł kryptografia.py , który zawiera funkcje do szyfrowania i
deszyfrowania tekstów za pomocą różnych metod kryptograficznych (np. szyfr
Cezara, szyfr Vigenère'a, szyfr XOR). Zaimportuj ten moduł do innego programu i
użyj go do szyfrowania i deszyfrowania przykładowych tekstów."""

from kryptografia import tKrypt

def main():
    #
    #
    # 2. kryptografia.py
    from kryptografia import tKrypt

    plain_text = "Once the command completes, you will be able to log into the server via SSH without being prompted for a password. However, if you set a passphrase when creating your SSH key, you will be asked to enter the passphrase at that time. This is your local ssh client asking you to decrypt the private key, it is not the remote server asking for a password."
    print("\n# 2.1 Szyfr Cezara")
    tKr2_1 = tKrypt(" Cezara", plain_text, 10 )
    # 2.1 Szyfr Cezara
    tKr2_1.caesar_encrypt_test()
    tKr2_1.caesar_decrypted_test()

    # 2.2 Vigenere
    print("\n# 2.2 Vigenere")
    tkr2_2 = tKrypt("Vigenere", plain_text, "EGx5HEXz7EqKigIxHHWKpCZItSj1Dy9Dqc5cYae+1zc" )
    tkr2_2.vigenere_encrypt_test()
    tkr2_2.vigenere_decrypt_test()

    # 2.3 XOR
    print("\n# 2.3 XOR")
    tkr2_3 = tKrypt("XOR", plain_text, "EGx5HEXz7EqKigIxHHWKpCZItSj1Dy9Dqc5cYae+1zc" )
    tkr2_3.xor_encryption_test()
    tkr2_3.xor_dencryption_test()

if __name__ == "__main__":
    main()