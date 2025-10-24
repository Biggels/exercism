import re

def is_pangram(sentence):
    sentence = re.sub(pattern = "[^A-Za-z]", repl = "", string = sentence)
    sentence = "".join(sentence.lower().split())
    return set(sentence) == set("abcdefghijklmnopqrstuvwxyz")
