# Written by *** for COMP9021
#
# Implements two functions that both return a string:
# - for line(), the equation of a line that goes through both points
#   provided as arguments;
# - for parabola(), the equation of a parabola that has as roots the
#   values provided as arguments.
def line(point_1, point_2):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    if point_1 == point_2:
        return None
    else:
        if x_1 == x_2:
            return f'x = {x_1:.2f}'
        else:
            k, b = (y_1 - y_2) / (x_1 - x_2), y_1 - (y_1 - y_2) / (x_1 - x_2) * x_1
            if y_1 == y_2:
                return f'y = {b:.2f}'
            elif b == 0:
                return f'y = {k:.2f}x'
            elif b > 0:
                return f'y = {k:.2f}x + {b:.2f}'
            elif b < 0:
                return f'y = {k:.2f}x - {-b:.2f}'
    return ''


def parabola(*roots):
    if roots:
        if len(set(roots)) == 1:
            if set(roots) == {0}:
                return f'x^2 = 0'
            else:
                b = roots[0] * -2
                c = roots[0] * roots[0]
                if b > 0:
                    return f'x^2 + {abs(b):}x + {c:} = 0'
                else:
                    return f'x^2 - {abs(b):}x + {c:} = 0'
        elif len(set(roots)) == 2:
            (x1, x2) = set(roots)
            b = - (x1 + x2)
            c = (x1 * x2)
            if b == 0:
                if c > 0:
                    return f'x^2 + {abs(c):} = 0'
                if c < 0:
                    return f'x^2 - {abs(c):} = 0'
            if c == 0:
                if b > 0:
                    if b == 1:
                        return f'x^2 + x = 0'
                    else:
                        return f'x^2 + {abs(b):}x = 0'
                if b < 0:
                    if b == -1:
                        return f'x^2 - x = 0'
                    else:
                        return f'x^2 - {abs(b):}x = 0'
            else:
                if b > 0 and c > 0:
                    if b == 1:
                        return f'x^2 + x+ {abs(c):} = 0'
                    else:
                        return f'x^2 + {abs(b):}x + {abs(c):} = 0'
                if b < 0 and c < 0:
                    if b == -1:
                        return f'x^2 - x- {abs(c):} = 0'
                    else:
                        return f'x^2 - {abs(b):}x - {abs(c):} = 0'
                if b > 0 and c < 0:
                    if b == 1:
                        return f'x^2 + x- {abs(c):} = 0'
                    else:
                        return f'x^2 + {abs(b):}x - {abs(c):} = 0'
                if b < 0 and c > 0:
                    if b == -1:
                        return f'x^2 - x+ {abs(c):} = 0'
                    else:
                        return f'x^2 - {abs(b):}x + {abs(c):} = 0'

        else:
            return None
    else:
        return None
    return ''


print(parabola(1, 0))
