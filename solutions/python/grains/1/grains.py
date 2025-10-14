def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return square(number - 1) * 2

def total_to_square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 2:
        return 3
    return square(number) + total_to_square(number - 1)

def total():
    return total_to_square(64)
