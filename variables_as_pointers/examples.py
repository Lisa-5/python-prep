# numbers = [1, 2, 3]
# # numbers2 = numbers

# # print(id(numbers) == id(numbers2))
# # print(numbers is numbers2)

# # print(id(numbers))
# # print(id(numbers2))

# # my_list = [[1, 2], 3, 4]
# # shallow = list(my_list)
# # print(shallow[0] is my_list[0])
# # print(shallow[0] == my_list[0])         # True

# # my_dict = {'abc': [1, 2, 3]}
# # shallow = dict(my_dict)
# # print(shallow['abc'] is my_dict['abc']) 
# # print(shallow['abc'] == my_dict['abc'])# True

# import copy

# orig = [[1, 2], 3, 4]
# dup = copy.copy(orig)

# print(orig is dup)           # False
# print(orig == dup)           # True
# orig[2] = 44
# print(dup)                   # [[1, 2], 3, 4]

# print(orig[0] is dup[0])     # True
# orig[0][1] = 22
# print(dup[0])                # [1, 22]   

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

# All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)           #False
print(dict1['a']    is dict2['a'])      #True
print(dict1['a'][0] is dict2['a'][0])   #True
print(dict1['a'][1] is dict2['a'][1])   #True
print(dict1['b']    is dict2['b'])      #True     
print(dict1['b'][0] is dict2['b'][0])   #True
print(dict1['b'][1] is dict2['b'][1])   #True