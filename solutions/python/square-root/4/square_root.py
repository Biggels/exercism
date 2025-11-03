import math

def square_root(number):
    m, e = math.frexp(number)
    n = math.ldexp(m, e // 2)

    while n * n != number:
        n = (n + number / n) // 2
        
    return n

        
