import re

def is_paired(input_string):
    bracket_string = re.sub(
        pattern = "[^[\]{}()]", 
        repl = "", 
        string = input_string
    )

    while re.search("\[\]|{}|\(\)", bracket_string):
        bracket_string = re.sub("\[\]|{}|\(\)", "", bracket_string)

    return bracket_string == ""
