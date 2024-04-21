# def find_first_nonzero_among(numbers):
#     for n in numbers:
#         if n != 0:
#             return n

# # print(find_first_nonzero_among([0, 0, 1, 0, 2, 0]))
# find_first_nonzero_among([1])

# import random

# def predict_weather():
#     sunshine = random.choice([True, False])

#     if sunshine:
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

# predict_weather()

# def multiply_by_five(n):
#     return n * 5

# # print("Hello! Which number would you like to multiply by 5?")
# number = int(input("Hello! Which number would you like to multiply by 5?\n"))

# print(f"The result is {multiply_by_five(number)}!")

# pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'].append('bowser')

# print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# def get_quote(person):
#     if person == 'Yoda':
#         return 'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         return 'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')

# numbers = []

# for i in range(1, 6):
#     numbers.append(i)

# print(numbers)

# info = {'name': 'Srdjan', 'age': 38}

# print(info.get('city', 'Unknown'))

# sub_list = ["-", "-", "-"]
# matrix = []

# for _ in range(3):
#     matrix.append(sub_list[:])

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# def find_maximum(numbers):
#     if not numbers:
#         return None
    
#     max_number = numbers[0]
#     for number in numbers:
#         if number > max_number:
#             max_number = number

#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0