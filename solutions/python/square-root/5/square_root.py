def square_root(number):
    n = 1 << number.bit_length() // 2

    while n * n != number:
        n = (n + number / n) // 2
        
    return n