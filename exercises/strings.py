# string = "These aren't the droids you're looking for."
# length_of_string = len(string)
# print(length_of_string)

# string = 'confetti floating everywhere'
# uppercased_string = string.upper()
# print(uppercased_string)

# string1 = "SS".lower()
# string2 = "ß".lower()
# print(string1)
# print(string2)
# print(string1 == string2)                         # False

# string1_casefolded = "SS".casefold()
# string2_casefolded = "ß".casefold()
# print(string1_casefolded)
# print(string2_casefolded)
# print(string1_casefolded == string2_casefolded)   # True

# rhyme = '''A pirate I was meant to be!
# Trim the sails and roam the sea!'''
# print(rhyme)
# print(rhyme.splitlines())

# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
# print('x' in char_sequence)

# def is_empty_or_blank(string):
#     return not string.strip(' ')
    
# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# def capitalize_words(string):
#     return string.title()

# string = 'launch school tech & talk'
# result = capitalize_words(string)
# print(result)

# def starts_with(string, prefix):
#     return string.startswith(prefix)

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

def count_substrings(string, substring):
    return string.casefold().count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0