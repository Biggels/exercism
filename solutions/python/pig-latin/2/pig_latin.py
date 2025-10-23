import re

def translate(text):
    pig_words = []
    pattern_rule_1 = re.compile(pattern = "^([aeiou]|xr|yt)", flags=re.IGNORECASE)
    pattern_rule_2 = re.compile(pattern = "^([bcdfghjklmnpqrstvwxyz]+)", flags=re.IGNORECASE)
    pattern_rule_3 = re.compile(pattern = "^([bcdfghjklmnpqrstvwxyz]*qu)", flags=re.IGNORECASE)
    pattern_rule_4 = re.compile(pattern = "^([bcdfghjklmnpqrstvwxyz]+)y", flags=re.IGNORECASE)
    for word in text.split():
        match_rule_1 = pattern_rule_1.match(word)
        match_rule_2 = pattern_rule_2.match(word)
        match_rule_3 = pattern_rule_3.match(word)
        match_rule_4 = pattern_rule_4.match(word)

        if match_rule_3:
            prefix = match_rule_3.group(1)
            rest = word[len(prefix):]
            pig_words.append(f"{rest}{prefix}ay")
            continue
        if match_rule_4:
            prefix = match_rule_4.group(1)
            rest = word[len(prefix):]
            pig_words.append(f"{rest}{prefix}ay")
            continue
        if match_rule_1:
            pig_words.append(f"{word}ay")
            continue
        if match_rule_2:
            prefix = match_rule_2.group(1)
            rest = word[len(prefix):]
            pig_words.append(f"{rest}{prefix}ay")
            continue
        pig_words.append(word)
    return " ".join(pig_words)
        
    
