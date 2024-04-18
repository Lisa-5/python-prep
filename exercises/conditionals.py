import random as r

# random_number = random.randint(0,1)

# if random_number:
#     print('Yes!')
# else: 
#     print('No.')

# print('Yes!' if random_number else 'No.')

weather = r.choice(['sunny', 'rainy', 'foggy', 'windy', 'snowy'])

# if weather == 'sunny':
#     print("It's a beautiful day!")
# elif weather == 'rainy':
#     print('Grab your umbrella.')
# else:
#     print("Let's stay inside.")

# animal = 'horse'

# match animal:
#     case 'duck':
#         print('quack')
#     case 'squirrel':
#         print('nook nook')
#     case 'horse':
#         print('neigh')
#     case 'bird':
#         print('tweet tweet')
#     case _:
#         print('*cricket*')

# match weather:
#     case 'sunny':
#        print("It's a beautiful day!") 
#     case 'rainy':
#         print('Grab your umbrella.')
#     case 'snowy':
#         print('Let\'s play in the snow!')
#     case _:
#         print('Let\'s stay inside.')
    
# if False or True:
#     print('Yes!')
# else:
#     print('No...')

# if True and False:
#     print('Yes!')
# else:
#     print('No...')

# sale = True
# admission_price = 5.25 if not sale else 3.99

# print(f"${admission_price}")

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)