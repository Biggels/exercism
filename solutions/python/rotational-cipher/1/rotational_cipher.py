from string import ascii_lowercase as ALPHABET

def rotate(text, key):
    cipher = ""

    for char in text:
        if char.lower() in ALPHABET:
            index = (ALPHABET.index(char.lower()) + key) % 26
            cipher_char = ALPHABET[index]
            if char.isupper():
                cipher += cipher_char.upper()
            else:
                cipher += cipher_char
        else:
            cipher += char

    return cipher
    

    
