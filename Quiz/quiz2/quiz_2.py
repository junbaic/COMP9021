# Written by *** for COMP9021
#
# Implements two functions that both return a string:
# - for line(), the equation of a line that goes through both points
#   provided as arguments;
# - for parabola(), the equation of a parabola that has as roots the
#   values provided as arguments.


def line(point_1, point_2):
    x1, y1, x2, y2 = point_1[0], point_1[1], point_2[0], point_2[1]
    a = 0
    b = 0
    x = 0
    y = 0
# 直线 y = a x + b
# 输入的两点相同，返None
    if point_1 == point_2:
        return None
# 两个点不同
    else:
# 线是垂直时
        if x1 == x2:
            return f"x = {x1:.2f}"
# 线是水平时
        else:
            if y1 == y2:
                return f"y = {y1:.2f}"
# 有斜率截距线
            else:
                a = (y1 - y2) / (x1 - x2)
                b = y1 - a * x1
                if b == 0:
                    return f"y = {a:.2f}x"
                else:
                    if b > 0:
                        return f"y = {a:.2f}x + {b:.2f}"
                    else:
                        return f"y = {a:.2f}x - {abs(b):.2f}"
#print(line((1,1),(2,2)))



# 抛物线 y = (x -x1)(x - x2)
# 不输入时return none


def parabola(*roots):
    set(roots)

# 没有或超过两个roots
    if len(set(roots)) == 0 or len(set(roots)) > 2:
        return None

# 有一个 roots
    if len(set(roots)) == 1:
        x3 = set(roots)
        b = (0 - 2) * list(x3)[0]
        c = list(x3)[0] ** 2
        if c == 0:
            return f"x^2 = 0"
        if b > 0:
            return f"x^2 + {int(b)}x + {int(c)} = 0"
        if b < 0:
            return f"x^2 - {abs(int(b))}x + {int(c)} = 0"

# 有两个roots
    else:
        if len(set(roots)) == 2:
            x1, x2 = set(roots)
    # 表示出 b c
            b = 0 - (x1 + x2)
            c = (x1 * x2)

    # y = x**2 + bx + c

    # y = x**2 + x
    #  b= +-1, c=0
            if abs(b)== 1 and c == 0:
                if b == 1:
                    return f"x^2 + x = 0"
                else:
                    return f"x^2 - x = 0"

    #  b= +-1, c<0
            if abs(b)== 1 and c < 0:
                if b == 1:
                    return f"x^2 + x - {abs(int(c))} = 0"
                else:
                    return f"x^2 - x - {abs(int(c))} = 0"
    #  b= +-1, c>0
            if abs(b)== 1 and c > 0:
                if b == 1:
                    return f"x^2 + x + {int(c)} = 0"
                else:
                    return f"x^2 - x + {int(c)} = 0"
    #  b= 0, c=0
            if b == 0 and c == 0:
                return f"x^2 = 0"
    #  b= 0, c<0
            if b == 0 and c < 0:
                return f"x^2 - {abs(int(c))} = 0"
    #  b= 0, c>0
            if b == 0 and c > 0:
                return f"x^2 + {int(c)} = 0"

    #  b< 0, c=0
            if b < 0 and c == 0:
                return f"x^2 - {abs(int(b))}x = 0"
    #  b< 0, c<0
            if b < 0 and c < 0:
                return f"x^2 - {abs(int(b))}x - {abs(int(c))} = 0"
    #  b< 0, c>0
            if b < 0 and c > 0:
                return f"x^2 - {abs(int(b))}x + {int(c)} = 0"
    #  b> 0, c=0
            if b > 0 and c == 0:
                return f"x^2 + {int(b)}x = 0"
    #  b> 0, c<0
            if b > 0 and c < 0:
                return f"x^2 + {int(b)}x - {abs(int(c))} = 0"
    #  b> 0, c>0
            else:
                return f"x^2 + {int(b)}x + {int(c)} = 0"
#print(parabola(-2.0,4.8))
    
    
    
