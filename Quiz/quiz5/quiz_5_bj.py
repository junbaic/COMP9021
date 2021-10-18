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

import sys

# INSERT YOUR CODE HERE
try:
    year_range = input('Input two distinct years in the range 1960 -- 2020: ').strip().split('--')
    if int(year_range[0]) > int(year_range[1]):
        year_range[0], year_range[1] = year_range[1], year_range[0]
    if len(year_range) != 2:
        raise ValueError
    else:
        if len(year_range[0].strip()) != 4 or len(year_range[1].strip()) != 4:
            raise ValueError
        if not year_range[0].strip().isdigit() or not year_range[1].strip().isdigit():
            raise ValueError
        if int(year_range[0]) == int(year_range[1]) or int(year_range[0]) < 1960 or int(year_range[1]) > 2020:
            raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()

N = int(input('Input a strictly positive integer: '))

if int(year_range[0]) < 1990 or int(year_range[1]) > 2016:
    print('I do not have data for any country for at least one of those years.')
else:
    dict_num1, dict_num2, dict_num3 = {}, {}, {}
    # 说不定可以用zip函数同时打开两个文件夹
    with open('./Areas/Agricultural Land/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_2056230.csv', 'r', encoding='UTF-8') as file1:
        for i, item in enumerate(file1):
            if i > 4:
                item1 = item.strip().split('","')
                num1 = item1[int(year_range[1]) - 1956].replace('"', '')
                num2 = item1[int(year_range[0]) - 1956].replace('"', '')
                if item1[int(year_range[0]) - 1956] != '' and item1[int(year_range[1]) - 1956] != '':
                    if float(num1) > float(num2):
                        name = item1[0].replace('"', '')
                        dict_num1[name] = float(num1) - float(num2)
    with open('./Areas/Forest/API_AG.LND.FRST.ZS_DS2_en_csv_v2_2125884.csv', 'r', encoding='UTF-8') as file2:
        for i, item_file2 in enumerate(file2):
            if i > 4:
                item1 = item_file2.strip().split('","')
                num1 = item1[int(year_range[1]) - 1956].replace('"', '')
                num2 = item1[int(year_range[0]) - 1956].replace('"', '')
                if item1[int(year_range[0]) - 1956] != '' and item1[int(year_range[1]) - 1956] != '':
                    if float(num1) > float(num2):
                        name = item1[0].replace('"', '')
                        dict_num2[name] = float(num1) - float(num2)

    for key1 in dict_num1.keys():
        for key2 in dict_num2.keys():
            if key1 == key2:
                dict_num3[key1] = (dict_num1[key1] / dict_num2[key2])
    list1 = sorted(dict_num3.values(), reverse=True)
    # 可以对list1进行切片操作 让list1的长度等于输入的N的长度 这样就不用分开考虑了
    i = 0
    if N <= len(list1):
        print(
            f'Here are the top {N} countries or categories where, between {year_range[0].strip()} '
            f'and {year_range[1].strip()},')
        print('  the ratios of agricultural land area and forest area')
        print('  (over total land) have both strictly increased,')
        print('  listed from the countries where the ratio of increases')
        print('  is largest, to those where it is smallest:')
        while i < N:
            for item in dict_num3:
                if dict_num3[item] == list1[i]:
                    print(f'{item} ({list1[i]:.2f})')
            i += 1
    else:
        print(
            f'Here are the top {len(list1)} countries or categories where, between {year_range[0].strip()} '
            f'and {year_range[1].strip()},')
        print('  the ratios of agricultural land area and forest area')
        print('  (over total land) have both strictly increased,')
        print('  listed from the countries where the ratio of increases')
        print('  is largest, to those where it is smallest:')
        while i < len(list1):
            for item in dict_num3:
                if dict_num3[item] == list1[i]:
                    print(f'{item} ({list1[i]:.2f})')
            i += 1
