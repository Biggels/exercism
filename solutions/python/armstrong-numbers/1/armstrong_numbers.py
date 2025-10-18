def is_armstrong_number(number):
    num_digits = len(str(number))
    sum = 0
    for digit in str(number):
        sum += int(digit) ** num_digits
    return sum == number
    
