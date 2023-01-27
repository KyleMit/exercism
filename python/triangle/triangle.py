def equilateral(sides):
    return isTriange(sides) and len(set(sides)) == 1


def isosceles(sides):
    return isTriange(sides) and len(set(sides)) <= 2


def scalene(sides):
    return isTriange(sides) and len(set(sides)) == 3


def isTriange(sides):
    return allSidesGreaterThanZero(sides) and twoSidesLessThanThird(sides)


def allSidesGreaterThanZero(sides):
    return all(s > 0 for s in sides)


def twoSidesLessThanThird(sides):
    a, b, c = sides
    return a + b >= c and a + c >= b and b + c >= a
