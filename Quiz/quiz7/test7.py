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
    grid = [[int(randrange(n) > 0) for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[int(randrange(-n) == 0) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
grid = np.array(grid)
directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

visit = []


def recursion(cur_y, cur_x):
    visit.append((cur_y, cur_x))
    for item in directions:
        next_x = cur_x + item[0]
        next_y = cur_y + item[1]
        if 0 <= next_x < dim and 0 <= next_y < dim:
            if grid[next_y][next_x] == 1:
                if (next_y, next_x) not in visit:
                    recursion(next_y, next_x)


total_chess = 0
for y in range(dim):
    for x in range(dim):
        if grid[y][x] == 1:
            if (y, x) not in visit:
                recursion(y, x)
                total_chess += 1
print()
if total_chess == 0:
    print("No chess knight has explored this board.")
if total_chess == 1:
    print("At least 1 chess knight has explored this board.")
if total_chess > 1:
    print(f"At least {total_chess} chess knights have explored this board.")
