import requests
from pprint import pprint 

# my_list = [6, 3, 0, 11, 20, 4, 17]

# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# print()

# for number in my_list:
#     print(number)

# index = 0
# while index < len(my_list):
#     number = my_list[index]
#     if number % 2 == 0:
#         print(number)
#     index += 1

# print()

# for number in my_list:
#     if number % 2 != 0:
#         print(number)

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]
     
# result = []
# for number in my_list:
#     if number % 2 == 0:
#         result.append('even')
#     else:
#         result.append('odd')

# result = [ 'even' if number % 2 == 0 else 'odd'
#           for number in my_list]
# print(result)

# def odd_or_even(number):
#     return 'even' if number % 2 == 0 else 'odd'

# result = [ odd_or_even(number)
#           for number in my_list ]
# print(result)

# def find_integers(iterable):
#     return [ element 
#              for element in iterable
#              if type(element) is int ]   

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# result = { element: len(element) 
#             for element in my_set 
#             if len(element) % 2 != 0 }

# print(result)

# def factorial(n):
#     result = 1
#     for number in range(1, n + 1):
#         result *= number

#     return result

# print(factorial(5))

import random

# highest = 10
# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break

# import random

# highest = 10
# number = random.randrange(highest + 1)
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for nested_list in my_list:
#     for number in nested_list:
#         if number % 2 == 0:
#             print(number)

