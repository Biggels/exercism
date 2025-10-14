def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    # number of grains on a square is equivalent to the binary number with a 1 in that position
    # 001 is 1
    # 010 is 2
    # 100 is 4
    # so we want to start with 001 and shift that 1 left for each square
    # (shift it 0 times for the first square since it's already correct, so number - 1)
    return 1 << (number - 1)

def total():
    # it's place value notation!
    # 100 is the number of grains on square 3
    # because a binary number is of the form 2^n + 2^n-1, etc.
    # 111 is 2^2 + 2^1 + 2^0, and that's exactly how we calculate the total number of grains on squares
    # so we just want the binary number composed of 64 bits (11111111111...1)
    # a simpler way to express that is just a 1 for the 65th bit, and then subtract 1 from that
    # so that's shifting the 1 over 64 times, then subtracting 1 from that binary number
    return (1 << 64) - 1
