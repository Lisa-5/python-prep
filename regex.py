import re

# def p(text):
#     print(re.findall(r'c.t$',
#           text,
#           flags=re.IGNORECASE))

# p("cat")         # ['cat']
# p("cot\n")       # ['cot']
# p("CATASTROPHE") # ['CAT']
# p("WILDCAUGHT")  # []
# p("wildcat\n")   # []
# p("-CET-")       # []
# p("Yacht")       # []

# def p(regex, text):
#     print(re.findall(regex,
#                      text,
#                      flags=re.IGNORECASE | re.MULTILINE))

# text = ("cat\ncot\nCATASTROPHE\nWILDCAUGHT\n" +
#         "wildcat\n-GET-\nYacht")

# p(r'\Ac.t', text)
# p(r'c.t\Z', text)

# def is_url(text):
#     return print(bool(re.search(r'^https?:\/\/\S+$', text)))

# is_url('https://launchschool.com')    # -> true
# is_url('http://example.com')          # -> true
# is_url('https://example.com hello')   # -> false
# is_url('   https://example.com')      # -> false

# def fields(text):
#     # text = text.replace(',', ' ')
#     return print(re.split(r'[ \t,]+', text))

# fields("Pete,201,Student");    # ['Pete', '201', 'Student']
# fields("Pete \t 201   ,  TA"); # ['Pete', '201', 'TA']
# fields("Pete \t 201");         # ['Pete', '201']
# fields("Pete \n 201");         # ['Pete', '\n', '201']

# def mystery_math(equation):
#     return print(re.sub(r'[+\-*\/]', '?', equation))

# mystery_math('4 + 3 - 5 = 2')
# # '4 ? 3 - 5 = 2'

# mystery_math('(4 * 3 + 2) / 7 - 1 = 1')
# # '(4 ? 3 + 2) / 7 - 1 = 1'

def danish(fruit):
    return print(re.sub(r'\b(apple|cherry|blueberry)\b', 'danish', fruit, count=1))

danish('An apple a day keeps the doctor away')
# -> 'An danish a day keeps the doctor away'

danish('My favorite is blueberry pie')
# -> 'My favorite is danish pie'

danish('The cherry of my eye')
# -> 'The danish of my eye'

danish('apple. cherry. blueberry.')
# -> 'danish. cherry. blueberry.'

danish('I love pineapple')
# -> 'I love pineapple'