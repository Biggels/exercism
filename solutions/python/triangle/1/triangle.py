def isTriangle(sides):
    a, b, c = sides
    return (a > 0) and (b > 0) and (c > 0) and (a + b >= c) and (b + c >= a) and (a + c >= b)
    

def equilateral(sides):
    print(isTriangle([0,0,0]))
    a, b, c = sides
    return isTriangle(sides) and a == b == c


def isosceles(sides):
    a, b, c = sides
    return isTriangle(sides) and (a == b or b == c or a == c)


def scalene(sides):
    return isTriangle(sides) and not equilateral(sides) and not isosceles(sides)
