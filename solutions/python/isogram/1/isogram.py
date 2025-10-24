import re

def is_isogram(string):
    string = re.sub(pattern = "[^A-Za-z]", repl = "", string = string).lower()
    used_letters = set()
    for letter in string:
        if letter in used_letters:
            return False
        used_letters.add(letter)
    return True
        
