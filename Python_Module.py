import random
import math
from random import randint
def subtract_5(A):
    return A - 5
def add_10(A):
    return A + 10
def multiply_2(A):
    return A * 2
def random(A):
    B = randint(1,5)
    return A + B

import PythonModule
print(PythonModule.subtract_5(10))
print(PythonModule.add_10(5))
print(PythonModule.multiply_2(4))
print(PythonModule.random(0))

print('We are going to find out whether or not you like candy')
Candy = input('Do you like candy? ')
if Candy == 'Yes':
    print('You like candy!')
elif Candy == 'No':
    print('You do not like candy...')
else:
    print('Please enter Yes or No.')

people_dictionary = {'Brett' : ['Male', 'Weight 175'], 'Nancy' : ['Female', 'Weight 125'], 'Patrick' : ['Male', 'Weight 195'], 'Brair' : ['Female', 'Weight 115'], 'Adam' : ['Male', 'Weight 215']}
print(people_dictionary)
