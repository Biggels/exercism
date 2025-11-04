from string import ascii_lowercase

ENCODE_MAP = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(plain_text, decode = False):
    plain_text = "".join(char.lower() for char in plain_text if char.isalnum())
    cipher_text = plain_text.translate(ENCODE_MAP)
    if decode:
        return cipher_text
    else:
        return " ".join(cipher_text[i:i+5] for i in range(0,len(cipher_text),5))

def decode(ciphered_text):
    return encode(ciphered_text, True)
