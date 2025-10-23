import re

def translate(text):
    pig_words = []
    for word in text.split():
        match_rule_1 = re.match(pattern = "^([aeiou]|xr|yt)", string = word)
        match_rule_2 = re.match(pattern = "^([bcdfghjklmnpqrstvwxyz]+)", string = word)
        match_rule_3 = re.match(pattern = "^([bcdfghjklmnpqrstvwxyz]*qu)", string = word)
        match_rule_4 = re.match(pattern = "^([bcdfghjklmnpqrstvwxyz]+)y", string = word)

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
    return " ".join(pig_words)
        
    
