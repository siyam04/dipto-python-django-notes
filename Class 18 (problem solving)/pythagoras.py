# imported built-in sqrt
from math import sqrt


def pythagoras(a, b):
    """Returning a pythagoras value"""
    if a <= 0 or b <= 0:
        return -1

    c = ('%.2f' % sqrt(a * a + b * b))
    return c


side_a, side_b = int(input('Enter first value:\n')), int(input('Enter second value:\n'))
print('Result is:', (pythagoras(side_a, side_b)))

