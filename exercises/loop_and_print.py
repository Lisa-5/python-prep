# for num in range(0, 11, 2):
#     print(num)

# for i in range(10, 0, -1):
#     print(i)

# print('Launch!')

# greeting = "Aloha!"

# for _ in range(3):
#     print(greeting)

# print()

# count = 1

# while count <= 3:
#     print(greeting)
#     count += 1
    
# for num in range(1, 101):
#     print(num * 2)

# lst = [1, 3, 7, 15]
# index = 0

# while index < len(lst):
#     for num in lst:
#         print(num)
#         index += 1

# while index < len(lst):
#     print(lst[index])
#     index += 1

# friends = ['Sarah', 'John', 'Hannah', 'Dave']

# for friend in friends:
#     print(f'Hello, {friend}!')

# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
#           'Vienna', None, 'London', 'Beijing', None]

# for city in cities: 
#     if city is None:
#         continue

#     print(f'{city}: {len(city)}')

# while True:
#     print("and on")
#     break

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break

# index = 0
# while index < len(fish_list):
#     print(fish_list[index])
#     if fish_list[index] == 'Nemo':
#         break
#     index += 1

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    