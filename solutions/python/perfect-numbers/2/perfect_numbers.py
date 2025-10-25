from math import sqrt, floor

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum({factor for factor in factors_of(number) if factor != number})
    match (number>aliquot_sum) - (number<aliquot_sum):
        case 1: return "deficient"
        case 0: return "perfect"
        case -1: return "abundant"

def factors_of(number):
    factors = set() 
    for factor in range(1, floor(sqrt(number)) + 1):
        quotient, remainder = divmod(number, factor)
        if remainder == 0:
            factors.add(factor)
            factors.add(quotient)
    return factors