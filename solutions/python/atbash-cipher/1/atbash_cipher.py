import re

PLAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHER_ALPHABET = "".join(char for char in reversed(PLAIN_ALPHABET))
ENCODE_MAP = str.maketrans(PLAIN_ALPHABET, CIPHER_ALPHABET)
DECODE_MAP = str.maketrans(CIPHER_ALPHABET, PLAIN_ALPHABET)

def encode(plain_text, map=ENCODE_MAP):
    plain_text = re.sub("[^a-zA-Z0-9]", "", plain_text).lower()
    cipher_text = plain_text.translate(map)
    cipher_text = " ".join(cipher_text[i:i+5] for i in range(0,len(cipher_text),5))
    return cipher_text


def decode(ciphered_text):
    plain_text = encode(ciphered_text, DECODE_MAP)
    return plain_text.replace(" ", "")
