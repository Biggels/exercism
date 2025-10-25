import math

def score(x, y):
    distance = math.hypot(x, y)
    boundaries = {
        10: 0,
        5: 1,
        1: 5
    }
    for boundary in boundaries:
        if distance > boundary:
            return boundaries[boundary]
    return 10
