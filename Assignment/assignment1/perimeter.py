# Insert your code here
file_name = input('Which data file do you want to use? ')
list_rectangle1, list_x, list_y = [], [], []
with open(f'{file_name}', 'r') as file:
    for line_items in file:
        for x in line_items.strip().split():
            x1, x2 = int((line_items.strip().split())[0]), int((line_items.strip().split())[2])
            y1, y2 = int((line_items.strip().split())[1]), int((line_items.strip().split())[3])
        list_rectangle1.append((x1, y1, x2, y2))
        list_x.append(x1)
        list_x.append(x2)
        list_y.append(y1)
        list_y.append(y2)
sort_list_x = sorted(set(list_x))
sort_list_y = sorted(set(list_y))
print(sort_list_x)
print(sort_list_y)
rect_top, rect_bottom, rect_left, rect_right = {}, {}, {}, {}
for item in list_rectangle1:
    rect_top[item] = ((item[0], item[3]), (item[2], item[3]))
    rect_bottom[item] = ((item[0], item[1]), (item[2], item[1]))
    rect_left[item] = ((item[0], item[1]), (item[0], item[3]))
    rect_right[item] = ((item[2], item[1]), (item[2], item[3]))
x_perimeter, y_perimeter = 0, 0
condition = [0, 0]
for index_y in range(1, len(sort_list_y)):
    for x in sort_list_x:
        for left_rect, right_rect in zip(rect_left.keys(), rect_right.keys()):
            if sort_list_y[index_y] > rect_left[left_rect][0][1]:
                if sort_list_y[index_y] <= rect_left[left_rect][1][1]:
                    if x == rect_left[left_rect][1][0]:
                        if condition[0] < 1:
                            y_perimeter = y_perimeter + (sort_list_y[index_y] - sort_list_y[index_y - 1])
                        condition[0] = condition[0] + 1
            if sort_list_y[index_y] > rect_right[right_rect][0][1]:
                if sort_list_y[index_y] <= rect_right[right_rect][1][1]:
                    if x == rect_right[right_rect][1][0]:
                        condition[0] -= 1
                        if condition[0] < 1:
                            y_perimeter = y_perimeter + (sort_list_y[index_y] - sort_list_y[index_y - 1])
print(y_perimeter)
for index_x in range(1, len(sort_list_x)):
    for y in sort_list_y:
        for bottom_points, top_points in zip(rect_bottom.values(), rect_top.values()):
            if sort_list_x[index_x] > bottom_points[0][0]:
                if sort_list_x[index_x] <= bottom_points[1][0]:
                    if y == bottom_points[1][1]:
                        if condition[1] < 1:
                            x_perimeter = x_perimeter + (sort_list_x[index_x] - sort_list_x[index_x - 1])
                        condition[1] = condition[1] + 1
            if sort_list_x[index_x] > top_points[0][0]:
                if sort_list_x[index_x] <= top_points[1][0]:
                    if y == top_points[1][1]:
                        condition[1] = condition[1] - 1
                        if condition[1] < 1:
                            x_perimeter = x_perimeter + (sort_list_x[index_x] - sort_list_x[index_x - 1])
print(x_perimeter)
print('The perimeter is:', x_perimeter + y_perimeter)



