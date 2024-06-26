# home_country = {
#     'Alice': 'USA',
#     'Francois': 'France',
#     'Inti': 'Peru',
#     'Monika': 'Germany',
#     'Sanyu': 'Uganda',
#     'Yoshitaka': 'Japan',
# }

# print(home_country['Alice'])
# print(home_country['Yoshitaka'])

# --------------------------------------
# Sum without highest and lowest number

# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

def sum_array(arr):
    if arr:
        return sum(sorted(arr)[1:-1])
    else:
        return 0

print(sum_array(None))
print(sum_array([]))
print(sum_array([3]))
print(sum_array([-3]))
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([6, 0, 1, 10, 10]))
print(sum_array([-6, -20, -1, -10, -12]))
print(sum_array([-6, 20, -1, 10, -12]))