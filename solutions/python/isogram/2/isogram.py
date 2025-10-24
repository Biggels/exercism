import re

def is_isogram(string):
    string = re.sub(pattern = "[^A-Za-z]", repl = "", string = string).lower()
    return len(string) == len(set(string))
        
