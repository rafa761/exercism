def equilateral(sides):
    if sum(sides) == 0:
        return False
    return sides[1:] == sides[:-1]


def isosceles(sides):
    if sum(sides) == 0:
        return False
    if (
        ((sides[0] + sides[1]) < sides[2])
        or ((sides[1] + sides[2]) < sides[0])
        or ((sides[0] + sides[2]) < sides[1])
    ):
        return False
    return len(set(sides)) in [2, 1]


def scalene(sides):
    if sum(sides) == 0:
        return False
    if ((sides[0] + sides[1]) < sides[2]) or ((sides[1] + sides[2]) < sides[0]) or ((sides[0] + sides[2]) < sides[1]):
        return False
    return len(set(sides)) == 3
