import re

def is_paired(input_string):
    stack = []
    matching_opener = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    for char in input_string:
        if char in "[{(":
            stack.append(char)
        elif char in "]})":
            if stack == []:
                return False
            if stack.pop() != matching_opener[char]:
                return False
        
    return True if stack == [] else False