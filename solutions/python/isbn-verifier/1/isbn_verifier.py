import re

def is_valid(isbn):
    pattern_match = re.fullmatch(pattern = "[0-9]-?[0-9]{3}-?[0-9]{5}-?[0-9|X]", string=isbn)
    if not pattern_match:
        return False

    isbn = list(isbn.replace("-", ""))
    if isbn[-1] == 'X':
        isbn[-1] = "10"
    isbn = [int(digit) for digit in isbn]
    
    check = sum([digit * (10-index) for index, digit in enumerate(isbn)]) % 11
    
    return not check
