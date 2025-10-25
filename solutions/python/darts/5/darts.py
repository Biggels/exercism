import math

def score(x, y):
    distance = math.hypot(x, y)
    return  (distance <= 10) * 1 + (distance <= 5) * 4 + (distance <= 1) * 5
