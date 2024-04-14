# How old are you? 27

# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()
# future_years = [10, 20, 30, 40] #range(10, 50, 10)

# for year in future_years:
#     print(f'In {year} years, you will be {age + year} years old.')
for future_year in range(10, 50, 10):
    print(f'In {future_year} years, you will be '
          f'{age + future_year} years old.')



