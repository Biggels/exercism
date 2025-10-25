import math

def score(x, y):
    distance = math.hypot(x, y)
    points = 0
    if distance <= 10:
        points += 1
    if distance <= 5:
        points += 4
    if distance <= 1:
        points += 5
    return points
