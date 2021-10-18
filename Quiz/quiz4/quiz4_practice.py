# Written by *** for COMP9021

# Prompts the user for 4 positive integers, the last three of which
# represent a number of points (nothing will need to be done if it is 0),
# an integer max_coordinate such that all coordinates to be generated
# will be between -max_coordinate and max_coordinate included, and a
# square window size (width and height).
#
# Generates a list of x coordinates and a list of y coordinates of common
# length the number of points requested. Shows these lists, possibly truncated.
#
# x-coordinates increase from left to right,
# y-coordinates increase from bottom to top.
#
# 1. Displays the points, without duplicates, from highest to lowest,
#    and from left to right for a given height.
#
# 2. Displays the size of the smallest rectangle, as well as its top left
#    and bottom right corners, in which all points fit.
#
# 3. Displays the maximum number of points that can fit in a square window
#    with the provided size. The window has to be fully included in the
#    enclosing rectangle. In case such a window exists, then displays the
#    top left and bottom right corners of the leftmost, topmost such window.
from time import sleep
from collections import defaultdict
from random import seed, randrange
import sys
import timeit

start = timeit.default_timer()

try:
    for_seed, nb_of_points, max_coordinate, window_size = \
        (int(e) for e in input('Enter four positive integers: ').split())
    sleep(0.01)
    if for_seed < 0 or nb_of_points < 0 or max_coordinate < 0 \
            or window_size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not nb_of_points:
    print('No point to play with, see you later!')
    sys.exit()
seed(for_seed)
x_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                 for _ in range(nb_of_points)
                 ]
y_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                 for _ in range(nb_of_points)
                 ]
field_width = max(max(len(str(e)) for e in x_coordinates),
                  max(len(str(e)) for e in y_coordinates)
                  )
print('Here is how the x-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in x_coordinates)
[: 80 // (field_width + 1) * (field_width + 1)]
      )
print('Here is how the y-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in y_coordinates)
[: 80 // (field_width + 1) * (field_width + 1)]
      )

# INSERT CODE HERE
print()
print('Here are the points, without duplicates, from highest to lowest,\n and from left to right for a given height:')
points = []
for x, y in zip(x_coordinates, y_coordinates):
    tuple1 = (x, y)
    points.append(tuple1)
points_sort = sorted(set(points), key=lambda x: (-x[1], x[0]))
for item in points_sort:
    print(f'  {item}')
print()
max_x, min_x, max_y, min_y = max(e for e in x_coordinates), min(e for e in x_coordinates), \
                             max(e for e in y_coordinates), min(e for e in y_coordinates)
size = abs(max_x - min_x) * abs(max_y - min_y)
print(f'All points fit in a rectangle of size {size},\n\
 with {(min_x, max_y)} as top left corner, and\n with {(max_x, min_y)} as bottom right corner.')
print()

dict1 = defaultdict(int)
for y in range(max_y, min_y - 1, -1):
    for x in range(min_x, max_x + 1):
        for x1, y1 in points_sort:
            if x <= x1 <= x + window_size and y - window_size <= y1 <= y:
                dict1[(x, y)] += 1
max_value = max(dict1.values())

list1 = []
if window_size <= size:
    for item in dict1.keys():
        if dict1[item] == max_value:
            list1.append(item)
    max_key = sorted(list1, key=lambda x: (-x[1], x[0]))
    point1 = max_key[0]
    point2 = (point1[0] + window_size, point1[1] - window_size)
    print(f'The maximum number of points that fit in a square window of size {window_size}\n\
 enclosed within the rectangle is {max_value}.\nThe leftmost, topmost such window has {point1} \
as top left corner,\n and {point2} as bottom right corner.')
else:
    print(f'The maximum number of points that fit in a square window of size {window_size}\n\
 enclosed within the rectangle is 0.')

end = timeit.default_timer()
print('time is %s' % (end - start))
