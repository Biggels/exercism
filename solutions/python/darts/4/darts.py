import math

def score(x, y):
    distance = math.hypot(x, y)
    scores = {
        distance <= 10: 1,
        distance <= 5: 5,
        distance <= 1: 10
    }
    return scores.get(True, 0)
