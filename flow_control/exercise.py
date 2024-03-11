# Exercise 1
False or (True and False)       # False
True or (1 + 2)             # True
(1 + 2) or True             # 3
True and (1 + 2)            # 3
False and (1 + 2)           # False
(32 * 4) >= 129                 # False
False != (not True)         # False
(True == 4)                     # False
False == (847 == '847')     # True


# Exercise 2
# integer = int(input('Enter an interger: '))

def even_or_odd(integer):
    print('even' if integer % 2 == 0 else 'odd')

    # if integer % 2 == 0:
    #     print('even')
    # else:
    #     print('odd')

# print(even_or_odd(integer))
# even_or_odd(4)
# even_or_odd(7)



# Exercise 3
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

# bar_code_scanner('113')
# bar_code_scanner(142)


# Exercise 4
# if foo():
#     return 'bar'
# else:
#     return qux()


# Exercise 5
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

# is_list_empty([])
# is_list_empty([0])
# is_list_empty([[]])
        
# Exercise 6
def transform_string(string):
    return (string.upper() if len(string) > 10 else string)

# print(transform_string('hello world'))
# print(transform_string('goodbye'))

# Exercise 7
def number_range(number):
    # if number < 0:
    #     print(f'{number} is less than 0')
    # elif number <= 50:
    #     print(f'{number} is between 0 and 50')
    # elif number <= 100:
    #     print(f'{number} is between 51 and 100')
    # else:
    #     print(f'{number} is greater than 100')

    if number > 100:
        print(f'{number} is greater than 100')
    elif number >= 50:
        print(f'{number} is between 51 and 100')
    elif number >= 0:
        print(f'{number} is between 0 and 50')
    else:
        print(f'{number} is less than 0')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0