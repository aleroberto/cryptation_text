def vigenere_encrypt(text, key, encryted_option):
    text = text.replace(" ", "").upper()
    key = key.upper()

    new_text = []
    key_length = len(key)
    crypted_char = None
    
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        key_shift = ord(key_char) - ord('A')

        if encryted_option == "cryp":
        	crypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
        else:
        	crypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))

        new_text.append(crypted_char)

    return ''.join(new_text)


def main():
	key = input("Forneca a chave:")
	encryted_option = input("cryp para criptografar ou encryp para o inverso")
	text = input("Digite o texto a ser criptografado: ")
    
	crypted_text = vigenere_encrypt(text, key, encryted_option)
	print(f"Texto retornado: {crypted_text}")

if __name__ == "__main__":
    main()



