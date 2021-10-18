# Uses data available at http://data.worldbank.org/indicator
# on Forest area (% of land area) and Agricultural land area (% of land area).
#
# Prompts the user for two distinct years between 1960 and 2020,
# separated by two consecutive hyphens with possibly spaces before
# and after, as well as a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area (as a ratio) has strictly increased from
#   oldest input year to most recent input year;
# - forest area (as a ratio) has strictly increased from oldest input
#   year to most recent input year;
# - the ratio of increase in agricultural land area to
#   increase in forest area (so a ratio of ratio differences)
#   determines output order.
#
# Countries are output from those whose ratio of increases is largest
# to those whose ratio of increases is smallest, as a floating point
# number with 2 digits after the decimal point.
#
# In the unlikely case where many countries share the same ratio
# of increases, countries are output in lexicographic order.
#
# In case fewer than N countries are found, only that number of
# countries is output.
#
# If no country has data for both years, then a special message is output.
#
# The data directory is stored in the working directory.


from collections import defaultdict
import csv
import os
from pathlib import Path
import sys
import sys

# INSERT YOUR CODE HERE
try:
    input_v = input('Input two distinct years in the range 1960 -- 2020: ')
    v = input_v.split('--')
    if len(v) != 2:
        raise ValueError
    else:
        second_year = v[1].strip()
        first_year = v[0].strip()
        if second_year.isdigit() and first_year.isdigit():
            if len(second_year) != 4 or len(first_year) != 4:
                raise ValueError
            if len(second_year) == 4 == len(first_year):
                second_year = int(second_year)
                first_year = int(first_year)
                # 第一个数据如果是在1960年之前或者2020年之后，则报错
                if first_year < 1960 or first_year > 2020:
                    raise ValueError
                # 两个年份相同不可以
                if second_year == first_year:
                    raise ValueError
                # 第二个数据如果是在1960年之前或者2020年之后，则报错
                if second_year < 1960 or second_year > 2020:
                    raise ValueError
        else:
            raise ValueError

except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit(0)

# 建字典
# 耕种面积
ag_area = dict()
p = int(input('Input a strictly positive integer: '))
if first_year > second_year:
    y=second_year
    second_year=first_year
    first_year =y
if first_year==1960 or second_year>2016:
    print('I do not have data for any country for at least one of those years.')
# 调用文件
if first_year>1960 and second_year<=2016:
    with open('./Areas/Agricultural Land/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_2056230.csv') as file:
        for l_number, line in enumerate(file):
            # 前5行空行文件
            if 5 <= l_number:
                information = line.strip().split('","')
                # 输入第一个年份对应的土地数据
                first_value = information[first_year - 1960 + 4].replace('"', '')
                # 输入第二个年份对应的土地数据
                second_value = information[second_year - 1960 + 4].replace('"', '')
                # 添加一个判断，令不为空值
                if second_value != '' and first_value != '':
                    # 第二个年份对应的土地数据大于第一个年份的的时候，表示出差值
                    if first_value < second_value:
                        second_value = float(second_value)
                        first_value = float(first_value)
                        country = information[0].replace('"', '')
                        ag_area[country] = second_value - first_value

    fo_area = dict()
    with open("./Areas/Forest/API_AG.LND.FRST.ZS_DS2_en_csv_v2_2125884.csv") as file:
        for l_number, line in enumerate(file):
            # 前5行空行文件
            if 5 <= l_number:
                information = line.strip().split('","')
                # 输入第一个年份对应的土地数据
                first_value = information[first_year - 1960 + 4].replace('"', '')
                # 输入第二个年份对应的土地数据
                second_value = information[second_year - 1960 + 4].replace('"', '')
                # 添加一个判断，令不为空值
                if second_value != '' and first_value != '':
                    # 第二个年份对应的土地数据大于第一个年份的的时候，表示出差值
                    if first_value < second_value:
                        second_value = float(second_value)
                        first_value = float(first_value)
                        country = information[0].replace('"', '')
                        fo_area[country] = second_value - first_value

    # 建字典
    # 森林面积
    r = {}
    for name, value in ag_area.items():
        if name in fo_area:
            r[name] = value / fo_area[name]
            # 把key和value打包，让字典变成元组的形式
            f = zip(r.keys(), r.values())
            # 对元组的value进行排序
            c = sorted(f, key=lambda k: [-k[1]])
    print(f"Here are the top {p} countries or categories where, between {first_year} and {second_year},")
    print('  the ratios of agricultural land area and forest area')
    print('  (over total land) have both strictly increased,')
    print('  listed from the countries where the ratio of increases')
    print('  is largest, to those where it is smallest:')
    if p <= len(c):
        for i in range(p):
            print(f"{c[i][0]} ({c[i][1]:.2f})")
    if p> len(c):
        print('I do not have data for any country for at least one of those years.')

