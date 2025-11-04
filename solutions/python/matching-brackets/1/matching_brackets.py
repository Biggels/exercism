import re

def is_paired(input_string):
    bracket_string = re.sub(
        pattern = "[^[\]{}()]", 
        repl = "", 
        string = input_string
    )
    while "[]" in bracket_string or "()" in bracket_string or "{}" in bracket_string:
        bracket_string = bracket_string.replace("[]", "").replace("{}", "").replace("()", "")

    return bracket_string == ""
