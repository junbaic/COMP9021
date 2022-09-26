# EDIT THE FILE WITH YOUR SOLUTION

# --------------------------Question1 preparation function---------------------------------------  #
# 给一个由坐标组成的List[(x1,y1),(x2,y2),(x3,y3)]
# 求出相邻两点的向量vector[],同一起点的向量sec_vector[],法向量fa_vector[]
# 判断fa_vector中的元素,大于0则往check[]中加1,小于0加0,等于0加2
# return check[]
def check_same_sign(item_piece):
    vector, sec_vector, fa_vector, check = [], [], [], []

    # 相邻的两个点连接成的向量全部加到vector里
    for index1 in range(len(item_piece) - 1):
        vector.append((item_piece[index1 + 1][0] - item_piece[index1][0],
                       item_piece[index1 + 1][1] - item_piece[index1][1]))
    # #最后一个点-->第一个点的向量
    vector.append((item_piece[0][0] - item_piece[-1][0], item_piece[0][1] - item_piece[-1][1]))

    # 后面的每个点与第一个点连接成的向量加到sec_vector里
    for index3 in range(1, len(item_piece)):
        sec_vector.append((item_piece[index3][0] - item_piece[0][0], item_piece[index3][1] - item_piece[0][1]))

    # 相邻的点的法向量全部加到fa_vector里
    for index2 in range(len(vector) - 1):
        fa_vector.append(vector[index2][0] * vector[index2 + 1][1] - vector[index2][1] * vector[index2 + 1][0])
    # #最后一个点与第一个点的法向量
    fa_vector.append(vector[-1][0] * vector[0][1] - vector[-1][1] * vector[0][0])

    # 后面的每个点与第一个点的法向量加到fa_vector里
    for index4 in range(1, len(sec_vector)):
        fa_vector.append(sec_vector[0][0] * sec_vector[index4][1] - sec_vector[0][1] * sec_vector[index4][0])

    for number in fa_vector:
        if number > 0:
            check.append(1)
        if number < 0:
            check.append(0)
        if number == 0:
            check.append(-1)
    return check


# 如果check [] 的长度为1 ,则fa_vector中都为同号
# return True(同号) or False(异号)
def check_sign(check):
    if len(set(check)) == 1:
        return True
    else:
        return False


# --------------------------Question2 preparation function ---------------------------------------  #

# 给两个坐标(x1,y1)(x2,y2)  return长度
def length(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


# 给一个包含坐标点的List[(x1,y1),(x2,y2),(x3,y3)]
# return一个包含边长的List[len,len,len,len,len,len]
def piece_length(graph):
    len1 = []
    for index_length in range(len(graph)):
        p1 = graph[index_length]
        p2 = graph[(index_length + 1) % len(graph)]
        p3 = graph[(index_length + 2) % len(graph)]
        len1.append(length(p1, p2))
        len1.append(length(p2, p3))
        len1.append(length(p3, p1))
    return len1


# 给两个包含边长的List，判断任何顺序下是不是相等的
# return True or False
def check_piece_length(len_1, len_2):
    if len(len_1) != len(len_2):
        return False
    else:
        for index_1 in range(len(len_1)):
            for index_2 in range(len(len_2)):
                if len_1[index_1] == len_2[index_2] and \
                        len_1[(index_1 + 1) % len(len_1)] == len_2[(index_2 + 1) % len(len_2)] and \
                        len_1[(index_1 + 2) % len(len_1)] == len_2[(index_2 + 2) % len(len_2)]:
                    i = 1
                    while i < len(len_1):
                        i += 1
                        if len_1[(index_1 + i) % len(len_1)] == len_2[(index_2 + i) % len(len_2)] and \
                                len_1[(index_1 + 1 + i) % len(len_1)] == len_2[(index_2 + 1 + i) % len(len_2)] and \
                                len_1[(index_1 + 2 + i) % len(len_1)] == len_2[(index_2 + 2 + i) % len(len_2)]:
                            continue
                        else:
                            break
                    else:
                        return True
        return False


# --------------------------Question3 preparation work ---------------------------------------  #
# 给一个由坐标组成的List[(x1,y1),(x2,y2),(x3,y3)]
# return 面积area
def get_area(List_points):
    a1 = 0
    a2 = 0
    for index in range(len(List_points)):
        a = List_points[index][0] * List_points[(index + 1) % len(List_points)][1]
        a1 += a
        b = List_points[(index + 1) % len(List_points)][0] * List_points[index][1]
        a2 += b
    area = abs(a1 - a2) * 0.5
    return area


# 给一个点和一个凸边形，判断这个点在不在凸边形的内部
# return True(inside) or False(outside)
def check_point_inside_convex(point, pieces):
    list1, list2 = [], []
    fa_vector_2 = []
    check_2 = []
    if 0 in (check_same_sign(pieces)) and len(set(check_same_sign(pieces))) == 1:
        pieces = pieces[::-1]
    for items in pieces:
        vector1 = (point[0] - items[0], point[1] - items[1])
        list1.append(vector1)
    for index in range(len(pieces)):
        vector2 = (pieces[(index + 1) % len(pieces)][0] - pieces[index][0],
                   pieces[(index + 1) % len(pieces)][1] - pieces[index][1])
        list2.append(vector2)
    for index in range(len(list1)):
        fa_vector_2.append(list2[index][0] * list1[index][1] - list2[index][1] * list1[index][0])
    for number in fa_vector_2:
        if number > 0:
            check_2.append(1)
        if number < 0:
            check_2.append(0)
        if number == 0:
            check_2.append(-1)
    if len(set(check_2)) == 1 and 1 in check_2:
        return True
    else:
        return False


def check_point_same_shape(points, shape):
    listx, listy, listx1, listy1 = [], [], [], []
    for item in shape:
        listx.append(item[0])
        listy.append(item[1])
    max_x, min_x, max_y, min_y = max(listx), min(listx), max(listy), min(listy)
    for item in points:
        listx1.append(item[0])
        listy1.append(item[1])
    max_x1, min_x1, max_y1, min_y1 = max(listx1), min(listx1), max(listy1), min(listy1)
    if max_x1 == max_x and min_x1 == min_x and max_y1 == max_y and min_y1 == min_y:
        return True


# --------------------------Main Function ----------------------------------------------------  #
class TangramPiecesError(Exception):
    pass


class TangramPieces:
    def __init__(self, filename):
        self.filename = filename
        self.all_piece = {}
        self.value = []

        self.available_coloured_pieces()
        self.are_valid()

    # 打开文件,获取每个piece的坐标放入piece_point[]           piece_point[]:[(x1,y1),(x2,y2),(x3,y3)]
    # line是读取到的每一行，list1代表将line切片成只包含坐标的[],line[-1]是包含颜色的字符串
    # 这个文件中所有pieces的坐标存入all_pieces[]    all_pieces[]:[[(x1,y1),(x2,y2),(x3,y3)],[(x1,y1),(x2,y2),(x3,y3)]]
    # return all_pieces[]
    def available_coloured_pieces(self):
        with open(self.filename) as fp:
            for line_number, line in enumerate(fp):
                line = line.strip().split()
                if line_number > 0 and len(line) > 6:
                    for index in range(len(line)):
                        if line[index] == 'd="M':
                            index_m = index
                        if line[index] == 'z"':
                            index_z = index
                    list1 = line[index_m + 1:index_z]
                    points = []
                    color = line[-1]
                    for index in range(2, len(list1) + 2, 3):
                        points.append((int(list1[index - 2]), int(list1[index - 1])))

                    if len(points) < 3:
                        raise TangramPiecesError('At least one piece is invalid')
                    else:
                        self.all_piece[color] = points

        return self.all_piece

    # 给一个包含了所有坐标的all_pieces[],判断其中的每一个single_piece是否是同号
    # return Ture or False
    def are_valid(self):
        for single_piece in self.all_piece.values():
            if len(single_piece) < 3:
                raise TangramPiecesError('At least one piece is invalid')
            elif check_sign(check_same_sign(single_piece)):
                self.value.append(1)
            else:
                self.value.append(0)
        if all(self.value):
            return True
        else:
            raise TangramPiecesError('At least one piece is invalid')

    def are_identical_to(self, anotherPiece):
        for colors, points_1 in self.all_piece.items():
            if len(self.all_piece.keys()) != len(anotherPiece.all_piece.keys()):
                return False
            if colors not in anotherPiece.all_piece.keys():
                return False
            else:
                points_2 = anotherPiece.all_piece[colors]
                if len(points_1) != len(points_2):
                    return False
                if check_piece_length(piece_length(points_1), piece_length(points_2)) \
                        or check_piece_length(piece_length(points_1), piece_length(points_2[::-1])) \
                        or check_piece_length(piece_length(points_1[::-1]), piece_length(points_2)) \
                        or check_piece_length(piece_length(points_1[::-1]), piece_length(points_2[::-1])):
                    continue
                else:
                    return False
        return True


class TangramShape:
    def __init__(self, file_name):
        self.file_name = file_name
        self.list_points = []
        self.get_list_points()

    def get_list_points(self):
        with open(self.file_name) as fp:
            for line_number, line in enumerate(fp):
                line = line.strip().split()
                if line_number > 0 and len(line) > 6:
                    for index in range(len(line)):
                        if line[index] == 'd="M':
                            index_m = index
                        if line[index] == 'z"':
                            index_z = index
                    list1 = line[index_m + 1:index_z]
                    for index in range(2, len(list1) + 2, 3):
                        self.list_points.append((int(list1[index - 2]), int(list1[index - 1])))
        return self.list_points

    def has_as_solution(self, other_file):
        result = []
        area1 = 0
        list_pointss = []
        for item in other_file.all_piece.values():
            area1 += get_area(item)
        if get_area(self.list_points) == area1:
            result.append(1)
        # 判断点是否在凸边形内部
        if len(other_file.all_piece.values()) > 1:
            for piece in other_file.all_piece.values():
                for item in piece:
                    list_pointss.append(item)
            for pieces in other_file.all_piece.values():
                for points in list_pointss:
                    if not check_point_inside_convex(points, pieces):
                        result.append(1)
                    else:
                        result.append(0)
            if check_point_same_shape(list_pointss, self.list_points):
                result.append(1)
            else:
                result.append(0)

        if len(set(result)) == 1 and 1 in result:
            return True
        else:
            return False
