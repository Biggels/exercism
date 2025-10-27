def rebase(input_base, digits, output_base):
    if not input_base >= 2:
        raise ValueError("input base must be >= 2")
    if not output_base >= 2:
        raise ValueError("output base must be >= 2")
    if not all([0 <= digit < input_base for digit in digits]):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    digits.reverse()
    num = sum([digit * input_base ** place for place, digit in enumerate(digits)])
    if num == 0:
        return [0]
    output_digits = []
    while num >= output_base:
        output_digits.append(num % output_base)
        num = num // output_base
    if num != 0: 
        output_digits.append(num)
    output_digits.reverse()
    return output_digits
        
        
    