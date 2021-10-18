# %load quiz_1.py
# Written by Jun Bai for COMP9021
#
# Given a sequence L of numbers, the greedy increasing subsequence of L,
# say G, is inductively defined as follows:
# - If L is of length at most 1 then G is L.
# - If L is of the form (e_0, e_1, ..., e_n) with n >= 1, then:
#   - either e_1 is greater than e_0, in which case G is e_0 followed by the
#     greedy increasing subsequence of (e_1, ..., e_n),
#   - or e_1 is less than or equal to e_0, in which case G is the greedy
#     increasing subsequence of (e_0, e_2,..., e_n).
#
# 1. Generates a random list L of digits whose length is chosen by the user
#    (done).
# 2. Displays L (done),
# 3. Displays the integer made from these digits (without the leading 0s,
#    if any).
# 4. Graphically displays the greedy increasing subsequence of L as
#    horizontal bars.
# 5. Graphically displays the nonzero values in L as steps.


from random import seed, randrange
import sys

try:
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                              ).split()
                        )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(10) for _ in range(length)]
print('Here are the generated digits:', values)
# INSERT CODE HERE:
print()
print('The integer made from these digits is: ', end='')
print(int(''.join(str(elem) for elem in values)))
print()
print('Here is the greedy increasing subsequence of values, '
      'horizontally displayed:\n'
      )
# INSERT CODE HERE:
#
a = 0
for elem in values:  # Use the for in loop to read the elements in list
    if elem > a:  # compare the value between element and a
        print('    ' + elem * '-')  # change the numbers to  -----  and print it
        a = elem
print('\nHere are the nonzero values, displayed as stairs:\n')
# INSERT CODE HERE:
b = 0
if 0 in values:  # remove 0 from the list
    values.remove(0)
for elem in values:
    if elem > 0:
        print('     ' + b * ' ' + elem * '-')
        b += elem
print()
