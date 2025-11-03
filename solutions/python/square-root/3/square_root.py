def square_root(number):
    n = number / 2

    while n * n != number:
        n = (n + number / n) // 2
        
    return n

        
