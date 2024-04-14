import requests 
from pprint import pprint 

squares = {f'{number}-squared': number * number 
           for number in range(1, 6)}
pprint(squares)

number_plus_one = { number + 1 for number in range(1, 6)}
print(number_plus_one)