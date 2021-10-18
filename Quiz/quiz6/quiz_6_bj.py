# Written by *** for COMP9021
#
# Randomly generates a grid with 0s and 1s, whose dimension is
# controlled by user input, as well as the density of 1s
# in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West)
# and for a given size greater than 1, the number of triangles
# pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size,
# the number of triangles pointing in that direction and of that size,
# provided there is at least one such triangle.
# For a given direction, the possible sizes are listed
# from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles,
# that is, obtained from the latter by ignoring at least one layer,
# starting from the base.


from random import seed, randint
import sys
import numpy as np
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                              for j in range(len(grid))
                              )
              )


try:
    arg_for_seed, density, dim = \
        (int(e) for e in input('Enter three nonnegative integers: ').split())
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()


# INSERT YOUR CODE HERE
def Solution(grid_n, fx):
    list1 = defaultdict(int)
    for y in range(dim):
        for x in range(dim):
            if grid_n[y][x] != 0:
                size = 1
                while y + size < dim:
                    if len(grid_n[y + size:y + size + 1, x - size:x + size + 1][0]) == (2 * (size + 1) - 1) and all(
                            grid_n[y + size:y + size + 1, x - size:x + size + 1][0]):
                        size += 1
                    else:
                        break
                if size >= 2:
                    list1[size] += 1
    list2 = sorted(list1.keys(), reverse=True)
    if list1:
        print()
        print(f"For triangles pointing {fx}, we have:")
        i = 0
        while i < len(list2):
            if list1[list2[i]] > 1:
                print(f"     {list1[list2[i]]} triangles of size {list2[i]}")
            else:
                print(f"     {list1[list2[i]]} triangle of size {list2[i]}")
            i += 1


if grid:
    grid1 = np.array(grid)
    grid2 = np.rot90(grid1)
    grid3 = np.rot90(grid2)
    grid4 = np.rot90(grid3)
    dict_direction = {'N': grid1, 'E': grid2, 'S': grid3, 'W': grid4}
    Solution(dict_direction['N'], 'N')
    Solution(dict_direction['E'], 'E')
    Solution(dict_direction['S'], 'S')
    Solution(dict_direction['W'], 'W')
