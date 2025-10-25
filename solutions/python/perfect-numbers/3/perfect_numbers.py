def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum({d for d in range(1, number) if number % d == 0})
    if number > aliquot_sum: return "deficient"
    if number == aliquot_sum: return "perfect"
    if number < aliquot_sum: return "abundant"