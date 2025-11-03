def square_root(number):
    start = 1
    stop = number
    n = start + ((stop - start) // 2)

    while n * n != number:
        if n * n < number:
            start = n
        elif n * n > number:
            stop = n
        n = start + ((stop - start) // 2)
    
    return n
        
