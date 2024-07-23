# plain_text = "Stwórz moduł kryptografia.py , który zawiera funkcje do szyfrowania i deszyfrowania tekstów za pomocą różnych metod kryptograficznych (np. szyfr Cezara, szyfr Vigenère'a, szyfr XOR). Zaimportuj ten moduł do innego programu i użyj go do szyfrowania i deszyfrowania przykładowych tekstów"
# key = "EGx5HEXz7EqKigIxHHWKpCZItSj1Dy9Dqc5cYae+1zc"

class tKrypt:
    def __init__(self, method_, plain_text_, key_):
        # self.z1 = z1_
        # self.z2 = z2_
        self.method = method_
        self.plain_text = plain_text_
        self.key = key_
        self.cipher_text = ""
        self.encrypted_text = ""
        self.powitanie()

    #
    # 1. szyfr Cezara
    #
    def caesar_encrypt(self, plain_text, key, decrypt=False):
        result = ""
        for character in plain_text:
            if character.isalpha():
                shift = key if not decrypt else -key
                if character.islower():
                    result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
                else:
                    result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
            else:
                result += character
        return result

    def caesar_encrypt_test(self):
        self.cipher_text = self.caesar_encrypt(self.plain_text, self.key)
        print("\n>> Encrypted Text (szyfr Cezara): {}".format(self.cipher_text))

    def caesar_decrypted_test(self):
        decrypted_text = self.caesar_encrypt(self.cipher_text, self.key, True)
        print("\n>> Decrypted Text (szyfr Cezara): {}".format(decrypted_text))

    #
    # 2. szyfr Vigenère'a
    #
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ''
        key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
        print("\n>> key_repeated: {}".format(key_repeated))
        print("\n>> plain_text: {}".format(plain_text))

        for i in range(len(plain_text)):
            if plain_text[i].isalpha():
                shift = ord(key_repeated[i].upper()) - ord('A')
                if plain_text[i].isupper():
                    encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += plain_text[i]
        return encrypted_text

    def vigenere_decrypt(self, cipher_text, key):
        decrypted_text = ''
        key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
        for i in range(len(cipher_text)):
            if cipher_text[i].isalpha():
                shift = ord(key_repeated[i].upper()) - ord('A')
                if cipher_text[i].isupper():
                    decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += cipher_text[i]
        return decrypted_text

    def vigenere_encrypt_test(self):
        self.cipher_text = self.vigenere_encrypt( self.plain_text, self.key)
        print("\n>> Encrypted Text (szyfr Vigenerea): {}".format(self.cipher_text))

    def vigenere_decrypt_test(self):
        decrypted_text = self.vigenere_decrypt(self.cipher_text, self.key)
        print("\n>> Decrypted Text (szyfr Vigenerea): {}".format(decrypted_text))

    #
    # 3. szyfr XOR
    #
    def xor_encryption(self, text, key):
        encrypted_text = ""
        for i in range(len(text)):
            encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
        return encrypted_text

    def xor_encryption_test(self):
        #plain_text = "Educative Accelerates Developer Productivity"
        #key = "Edu_key"
        #encrypted_text = xor_encryption(plain_text, key)
        self.encrypted_text = self.xor_encryption(self.plain_text, self.key)
        print(">> Encrypted Text (szyfr XOR): {}".format(self.encrypted_text))

    # Decrypting the Text
    def xor_dencryption_test(self):
        decrypted_text = self.xor_encryption(self.encrypted_text, self.key)
        print(">> Decrypted Text (szyfr XOR): {}".format(decrypted_text))




    def powitanie(self):
        print(">>")
        print(">> Modul kryptografia: {}".format(self.method))
        print(">>")
        #print(">> moduł kryptografia: [{}, {}]".format(self.z1, self.z2))