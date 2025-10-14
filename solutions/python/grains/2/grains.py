def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    total = 0
    n = 64
    while n >=1:
        total += square(n)
        n -= 1

    return total
