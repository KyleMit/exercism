def score(x, y):
    xy_radius = x**2 + y**2
    if xy_radius <= 1**2:
        return 10
    elif xy_radius <= 5**2:
        return 5
    elif xy_radius <= 10**2:
        return 1
    else:
        return 0
