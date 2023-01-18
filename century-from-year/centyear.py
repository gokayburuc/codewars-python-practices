import math


def century(year):
    # cent = int(round(year / 100, 0) + 1)
    cent = math.ceil(year/100)
    return cent
