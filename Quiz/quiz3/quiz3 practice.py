# Written by *** for COMP9021

# Prompts the user for two integers.
# - The first one should be between 1 and 4, with
#   * 1 meaning initially looking North,
#   * 2 meaning initially looking East,
#   * 3 meaning initially looking South,
#   * 4 meaning initially looking West.
# - The second one should be positive. When written in base 3, its consecutive
#   digits read from left to right represent the directions to take, with
#   * 0 meaning going in the direction one is initially looking at,
#   * 1 meaning 45 degrees left of the direction one is initially looking at,
#   * 2 meaning 45 degrees right of the direction one is initially looking at.
#
# Prints out:
# - the direction one is originally looking at, as an arrow,
# - the representation of the second digit in base 3,
# - the corresponding sequence of directions to take, as arrows,
# - in case one is originally looking North or South, the path,
#   so the sequence of arrows again, but nicely displayed.


import sys

try:
    initial_direction, directions = input('Enter an integer between 1 and 4 '
                                          'and a positive integer: '
                                          ).split()
    if len(initial_direction) != 1 \
            or len(directions) > 1 and directions[0] == '0':
        raise ValueError
    initial_direction = int(initial_direction)
    directions = int(directions)
    if initial_direction not in {1, 2, 3, 4} or directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# INSERT YOUR CODE HERE
dict_arrow = {1: chr(8679), 2: chr(8680), 3: chr(8681), 4: chr(8678)}
print()
print('Ok, you want to first look this way:', dict_arrow[initial_direction])
print()
list_3 = []
while directions >= 0:
    x, y = divmod(directions, 3)
    list_3.append(str(y))
    directions = x
    if directions == 0:
        break
base_3 = list_3[::-1]
print('In base 3, the second input reads as:', ''.join(base_3))
list_arrow = []
dict1 = {'0': chr(8679), '1': chr(11009), '2': chr(11008)}
dict2 = {'0': chr(8680), '1': chr(11008), '2': chr(11010)}
dict3 = {'0': chr(8681), '1': chr(11010), '2': chr(11011)}
dict4 = {'0': chr(8678), '1': chr(11011), '2': chr(11009)}
dict_new = {1: dict1, 2: dict2, 3: dict3, 4: dict4}
for string in base_3:
    list_arrow.append(dict_new[initial_direction][string])
print('So that\'s how you want to go: ', ''.join(list_arrow))
print()
list1 = []
list2 = []
list3 = []
list4 = []
if initial_direction == 1:
    print('Let\'s go then!')
    x = 0
    index = -1
    directions = {'0': 0, '1': -1, '2': 1}
    for item in base_3:
        x = x + directions[item]
        list1.append(x)
    if min(list1) != 0:
        value = 0 - min(list1)
        for i in list1:
            i = i + value
            list2.append(i)
        for arrow in list_arrow[::-1]:
            print(' ' * list2[index] + arrow)
            index = index - 1
    if min(list1) == 0:
        for arrow in list_arrow:
            print(' ' * list1[index] + arrow)
            index = index - 1

if initial_direction == 2:
    print('I don\'t want to have the sun in my eyes, but by all means have a go at it!')
if initial_direction == 3:
    print('Let\'s go then!')
    x = 0
    index = 0
    directions2 = {'0': 0, '1': 1, '2': -1}
    for item in base_3:
        x = x + directions2[item]
        list3.append(x)
    if min(list3) != 0:
        value = 0 - min(list3)
        for i in list3:
            i = i + value
            list4.append(i)
        for arrow in list_arrow:
            print(' ' * list4[index] + arrow)
            index = index + 1
    if min(list3) == 0:
        for arrow in list_arrow:
            print(' ' * list3[index] + arrow)
            index = index + 1
if initial_direction == 4:
    print('I don\'t want to have the sun in my eyes, but by all means have a go at it!')
