from math import sqrt, floor

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    factors = factors_of(number)
    factors.remove(number)
    aliquot_sum = sum(factors)
    # try (a>b) - (a<b) and match
    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum:
        return "deficient"

def factors_of(number):
    factors = set() 
    for factor in range(1, floor(sqrt(number)) + 1):
        quotient, remainder = divmod(number, factor)
        if remainder == 0:
            factors.add(factor)
            factors.add(quotient)
    return factors