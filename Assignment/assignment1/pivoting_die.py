# Insert your code here
import math

while True:
    try:
        N = int(input('Enter the desired goal cell number: '))
        if N <= 0 or N == '':
            raise ValueError
        else:
            break
    except ValueError:
        print('Incorrect value, try again')

dict_opposite, top_number, front_number, right_number = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}, 3, 2, 1
position_N = 2
while position_N <= N:
    # take the square root of N and round it down to get the number of cycles n
    n = int(math.sqrt(position_N))
    # if n is even, take n-1 which is the last cycle of n
    if n % 2 != 1:
        n -= 1
    # when n is on a special point, take n-2
    elif n ** 2 <= position_N <= n ** 2 + 1:
        n -= 2
    # periodic point_12345
    point_1, point_2, point_3 = n ** 2 + 1, (n + 1) * n + 1, (n + 1) ** 2 + 1
    point_4, point_5 = (n + 1) * (n + 2) + 1, (n + 2) ** 2 + 1
    # turn down
    if point_1 < position_N <= point_2:
        front_opposite, front_number = dict_opposite[front_number], top_number
        top_number, right_number = front_opposite, right_number
    # turn left
    elif point_2 < position_N <= point_3:
        top_opposite, top_number = dict_opposite[top_number], right_number
        right_number, front_number = top_opposite, front_number
    # turn up
    elif point_3 < position_N <= point_4:
        top_opposite, top_number = dict_opposite[top_number], front_number
        front_number, right_number = top_opposite, right_number
    # turn right
    elif point_4 < position_N <= point_5:
        right_opposite, right_number = dict_opposite[right_number], top_number
        top_number, front_number = right_opposite, front_number

    if position_N > 2:
        if position_N == point_1 + 1:
            if point_2 - point_1 >= 4:
                position_N += (((point_2 - point_1) // 4) * 4) if N > point_2 else (((N - position_N) // 4) * 4)
            else:
                position_N = position_N
        if position_N == point_2:
            if point_3 - point_2 >= 4:
                position_N += (((point_3 - point_2) // 4) * 4) if N > point_3 else (((N - position_N) // 4) * 4)
            else:
                position_N = position_N
        if position_N == point_3:
            if point_4 - point_3 >= 4:
                position_N += (((point_4 - point_3) // 4) * 4) if N > point_4 else (((N - position_N) // 4) * 4)
            else:
                position_N = position_N
        if position_N == point_4:
            if point_5 - point_4 >= 4:
                position_N += (((point_5 - point_4) // 4) * 4) if N > point_5 else (((N - position_N) // 4) * 4)
            else:
                position_N = position_N
    else:
        pass
    position_N += 1
print(f'On cell {N}, {top_number} is at the top, {front_number} at the front, and {right_number} on the right.')
