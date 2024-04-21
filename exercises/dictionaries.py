from pprint import pprint

# car = {
#     'type': 'sedan',
#     'color': 'blue',
#     'mileage': 80000,
# }

# print(car)

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2003

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }

# del car['mileage']
# print(car)

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(car['color'])
# print(car.get('year'))

# print(len(car))

# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print('name' in student)
# print('grade' in student)

# vehicles = {
#     'car': {
#         'type':  'sedan',
#         'color': 'blue',
#         'year':  2003,
#     },

#     'truck': {
#         'type':  'pickup',
#         'color': 'red',
#         'year':  1998,
#     },
# }

# print(vehicles['car']['color'])

# car = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# half_numbers = []

# for number in numbers.values():
#     half_numbers.append(number //2)

# print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f'A {key} number is {value}.')