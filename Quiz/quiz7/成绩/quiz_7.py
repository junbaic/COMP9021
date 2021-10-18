# Written by *** for COMP9021
#
# Randomly fills an array of size 10x10 with True and False,
# displayed as 1 and 0, and outputs the number of chess knights
# needed to jump from 1s to 1s and visit all 1s (they can jump back
# to locations previously visited).


from random import seed, randrange
import sys
import numpy as np

dim = 10


def display_grid():
    for row in grid:
        print('    ', ' '.join(str(int(e)) for e in row))


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        n = 1
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
grid = np.array(grid)
directions = {'N': (1, 2), 'NE': (2, 1), 'E': (2, -1), 'ES': (1, -2), 'S': (-1, -2), 'SW': (-2, -1), 'W': (-2, 1),
              'NW': (-1, 2)}
knights = 0
dp = []


def check(x1, y1):
    if grid[x1, y1]:
        return True


def jump(cur_y, cur_x):
    dp.append((cur_y, cur_x))
    for item in directions.values():
        if 0 <= cur_y < dim:
            if 0 <= cur_x < dim:
                if 0 <= cur_y + item[1] <= dim - 1:
                    if 0 <= cur_x + item[0] <= dim - 1:
                        if check(cur_y + item[1], cur_x + item[0]):
                            if (cur_y + item[1], cur_x + item[0]) not in dp:
                                jump(cur_y + item[1], cur_x + item[0])
    return True


for y in range(dim):
    for x in range(dim):
        if check(y, x) and (y, x) not in dp:
            knights += 1
            if jump(y, x):
                continue

print()
if knights > 1:
    print(f"At least {knights} chess knights have explored this board.")
else:
    print_words = {0: "No chess knight has explored this board.",
                   1: "At least 1 chess knight has explored this board."}
    print(print_words[knights])
