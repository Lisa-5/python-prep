# def top():
#     bottom()

# def bottom():
#     print('Reached the bottom')

# top()

# def foo():
#     def bar():
#         print('BAR')

#     bar() # BAR

# foo()
# # bar() # NameError: name 'bar' is not defined

# greeting = 'Salutations'

# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

# def outer():
#     def inner1():
#         def inner2():
#             foo = 3
#             print(f"inner2 -> {foo} with id {id(foo)}")

#         foo = 2
#         inner2()
#         print(f"inner1 -> {foo} with id {id(foo)}")

#     foo = 1
#     inner1()
#     print(f"outer -> {foo} with id {id(foo)}")

# outer()

# from math import sqrt, pi

# print(sqrt(pi))
# print(pi)

# def sum_of_squares(num1, num2):
#     def square(number):
#         return number * number
    
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# counter = 0
# def increment_counter():
#     global counter
#     counter += 1

# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()