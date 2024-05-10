'''
print('abc' == 'aBc')
print('abc'.lower() == 'aBc'.lower())
print('abc'.upper() == 'aBC'.upper())
'''

"""
print(5 != 5)
print(5 != 4)
print('abc' != 'abc')
print('abc' != 'aBC')
print(5 != '5')
"""

# value = 0                     # 0 is falsy
# if value:
#     print(f'{value} is truthy')
# else:
#     print(f'{value} is falsy')

# print(3 and 'foo')   # last evaluated op: 'foo'
# print('foo' and 3)   # last evaluated op: 3
# print(0 and 'foo')   # last evaluated op: 0
# print('foo' and 0)   # last evaluated op: 0



# value = 3

# match value:
#     case 1 | 2 | 3 | 4:
#         print('value is < 5')
#     case 5 | 6:
#         print('value is 5 or 6')
#     case _: # default case
#         print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6

# names = ['Karl', 'Grace', 'Clare', 'Victor',
#          'Antonina', 'Allison', 'Trevor', 'Clare']
# print(names.index('Clare'))   # 2
# print(names.index('Trevor'))  # 6
# print(names.count('Chris'))
# print(names.count('Clare'))
# ValueError: 'Chris' is not in list

# result = zip(range(5, 10),    # length is 5
#              range(1, 3),     # length is 2 (shortest)
#              range(3, 7),
#              strict=True)     # length is 4
# print(list(result)) # [(5, 1, 3), (6, 2, 4)]

# text = ' \t  abc def    \n\r'
# print(repr(text.strip('abc'))) # ' \t  abc def    \n\r'

# text = 'aaabaacccabxyzabccba'
# print(text.strip('a'))         # baacccabxyzabccb
# print(text.strip('ab'))        # cccabxyzabcc
# print(text.strip('ba'))        # cccabxyzabcc
# print(text.strip('abc'))       # xyz
# print(text.strip('bc'))        # aaabaacccabxyzabccba

# print(repr(text.strip('abcxyz'))) # ''
from pprint import pprint 
# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# ranks = [
#     '2', '3', '4', '5', '6', '7', '8', '9', '10',
#     'Jack', 'Queen', 'King', 'Ace',
# ]

# deck = []
# for suit in suits:
#     for rank in ranks:
#         card = f'{rank} of {suit}'
#         deck.append(card)

# pprint(deck)

# numbers = [1, 2, 3]
# numbers2 = numbers

# print(id(numbers))
# print(id(numbers) == id(numbers2))
# print(numbers is numbers2)

# def top():
#     bottom()

# def bottom():
#     print('Reached the bottom')

# top()

# top()

# def top():
#     bottom()

# def bottom():
#     print('Reached the bottom')

# from math import sqrt 

# print(sqrt(37))

# import re

# mystr = 'cast'

# if re.search(r's', mystr):
#     print("matched 's'")

# if re.search(r'x', mystr):
#     print("matched 'x'")

import re

text = "Four score"
text2 = "Four\tscore"
text3 = "Four-score\n"
text4 = "Four-score"
text5 = 'a b'
text6 = " \t\n\r\f\v"

if re.search(r'\s', text):
    print("matched 1")
if re.search(r'\s', text2):
    print("matched 2")
if re.search(r'\s', text3):
    print("matched 3")
if re.search(r'\s', text4):
    print("matched 4")
if re.search(r'\S', text5):
    print("matched 5")
if re.search(r'\S', text6):
    print("matched 6")
# print(text)