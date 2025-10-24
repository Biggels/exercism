from string import ascii_lowercase as ALPHABET

def rotate(text, key):
    cipher = ""
    
    ALPHABET_ROT = ALPHABET[key:] + ALPHABET[:key]
    ALPHABET_MAP = dict(zip(ALPHABET, ALPHABET_ROT))
    print(ALPHABET_MAP)

    for char in text:
        if char.lower() not in ALPHABET_MAP:
            cipher += char
        else:
            if char.isupper():
                cipher += ALPHABET_MAP[char.lower()].upper()
            else:
                cipher += ALPHABET_MAP[char]

    return cipher
    

    
