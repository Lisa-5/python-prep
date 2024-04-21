# def first(lst):
#     if lst:
#         return lst[0]

# print(first(['Earth', 'Moon', 'Mars']))  # Earth
# print(first([]))

# def last(lst):
#     if lst:
#         return lst[-1]
    
# print(last(['Earth', 'Moon', 'Mars']))  # Earth
# print(last([]))

# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# print(energy)
# print(type(energy.remove('fossil')))
# print(type(energy.append('geothermal')))
# print(energy)

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(list(alphabet))

# scores = [96, 47, 113, 89, 100, 102]

# count = 0

# for score in scores:
#     if score >= 100:
#         count += 1

# print(count)

# high_scores = [score for score in scores if score >= 100]
# print(type(high_scores))
# print(len(high_scores)) # 3

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for grouping in vocabulary:
#     for word in grouping:
#         print(word)

# # happy
# # cheerful
# # merry
# # glad
# # tired
# # sleepy
# # etc...

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# print(isinstance(some_value1, list))
# print(isinstance(some_value2, list))

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# def contains(element, lst):
#     return lst.count(element) > 0

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# print('-'.join(passcode))
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
# joined_passcode = ''

# for i in range(len(passcode)):
#     if i > 0:
#         joined_passcode += '-'

#     joined_passcode += passcode[i]

# print(joined_passcode)  # 11-jZ5-hQ3f*-8!7g3-p3Fs

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)
    print((grocery_list))