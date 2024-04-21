# def multiply(number1, number2):
#     return number1 * number2

# print(multiply(12, 4))

# def bruce_eckel_quote():
#     print('Python is executable pseudocode.')

# print(bruce_eckel_quote())

# def cite(author, quote):
#     print(f'{author} said: "{quote}"')

# cite('Bruce Eckel', 'Python is executable pseudocode.')

# def squared_number(number):
#     return number**2

# print(squared_number(3))

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three()

# def compare_by_length(str1, str2):
#     if len(str1) < len(str2):
#         return -1
#     elif len(str1) > len(str2):
#         return 1
#     else:
#         return 0

# print(compare_by_length('patience', 'perseverance')) # -1
# print(compare_by_length('strength', 'dignity')) #  1
# print(compare_by_length('humor', 'grace')) #  0

# print('Captain Ruby'.replace('Ruby', 'Python'))
# print("Captain Ruby".split(' ')[0] + ' Python')

def greet(launguage_code):
    match launguage_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Ola!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

# print(greet('en'))         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!

def extract_language(locale):
  return locale[:2]

# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))   
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!    # Howdy!