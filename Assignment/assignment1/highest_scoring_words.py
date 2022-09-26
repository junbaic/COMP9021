# Insert your code here
import sys
from collections import defaultdict

try:
    letter1 = input('Enter between 3 and 10 lowercase letters: ')
    letter2 = letter1.replace(' ', '')
    if not letter1.islower() or not letter1.isalpha():
        raise ValueError
    if len(letter2) > 10 or len(letter2) < 3:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()


def check_input_txt(input1, txt):
    flag = True
    for characters in txt:
        if input1.count(characters) < txt.count(characters):
            flag = False
            break
    return flag


list_words = []
with open("wordsEn.txt", 'r') as file1:
    for items in file1:
        if check_input_txt(letter2, items.strip()):
            list_words.append(items.strip())

dict_score = {'a': 2, 'b': 5, 'c': 4, 'd': 4, 'e': 1, 'f': 6, 'g': 5, 'h': 5, 'i': 1,
              'j': 7, 'k': 6, 'l': 3, 'm': 5, 'n': 2, 'o': 3, 'p': 5, 'q': 7, 'r': 2,
              's': 1, 't': 2, 'u': 4, 'v': 6, 'w': 6, 'x': 7, 'y': 5, 'z': 7}

dict_high_score = defaultdict(int)
for words in list_words:
    for word in words:
        dict_high_score[words] += dict_score[word]
if dict_high_score:
    max_value = max(dict_high_score.values())
    print(f'The highest score is {max_value}.')
    list1 = []
    for item in dict_high_score.keys():
        if dict_high_score[item] == max_value:
            list1.append(item)
    if len(list1) == 1:
        print(f'The highest scoring word is {list1[-1]}')
    else:
        print('The highest scoring words are, in alphabetical order:')
        for item1 in list1:
            print(f'    {item1}')
else:
    print('No word is built from some of those letters.')
