import math

def score(x, y):
    distance = math.hypot(x, y)
    boundaries = {
        10: 0,
        5: 1,
        1: 5
    }
    for boundary, points in boundaries.items():
        if distance > boundary:
            return points
    return 10
