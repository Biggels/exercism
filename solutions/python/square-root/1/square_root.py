def square_root(number):
    for s in range(1, number // 2 + 2):
        print(s)
        if s * s == number:
            return s
        
