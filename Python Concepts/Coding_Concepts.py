J = 50
K = 5
print(J + K)
J = 50
K = 5
print (J + K)

if J > 25:
    print ("J is the winner")

B = 20
if B == 20:
    print("20 is equal to B")

name1 = 'Ashley'
print(name1.upper())
name2 = 'Bob'
print(name2.lower())

print(name1[0])
print(name2[2])

listA = ["mother", "father", "1970", "1965"]
print(listA[3])

tupA = ("brother", "sister", "1990", "1992", "1993", "1995")
print(tupA[1:4])

date = "03/13/2021"
split_the_date = date.split('/')
print(split_the_date)
print(split_the_date[0])
print(split_the_date[1])
print(split_the_date[2])

print("Month: " + split_the_date[0])
print("Day: " + split_the_date[1])
print("Year: " + split_the_date[2])

date = "12/25/2025"
full_date = date.split('/')
print('Month: ' + full_date[0] + 'Day: ' + full_date[1] + 'Year: ' + full_date[2])

Name = "Jack"
Name.swapcase()

Color_1 = '  red  '
Color_2 = '         blue         '
print('My favorite colors are ' + Color_1.strip() + ' and ' + Color_2.strip())

B = "Let's do some math!"
print(B)
X = 10
print("X = 10")
print("X plus 5 equals:")
print(X + 5)
A = 5
print("A = 5")
print("A minus X equals:")
print(X - A)
print("X times A equals:")
print(X * A)
print("X divided by A equals:")
print(X/A)
print("Is X larger than A?:")
print(X > A)
print("Is X less than A?:")
print(X < A)
print(X == A)
if X > A:
    print("X is larger than A")
name = 'BILLY'
print(name)
print("Now it is time to print BILLY in all lower case letter: " + name.lower())
list_names = ['Billy', 'Sally', 'Johnny', 'Raphael']
print("Here's the list created: ")
print(list_names)
print("Here's the third name from the list we wrote in all caps: " + list_names[2].upper())
date = "July/14th/1987"
print("Here's the date we created: " + date)
split_date = date.split('/')
print("Here's the date we created split apart: ")
print(split_date)
another_name = 'DiAnE'
print("We chose the name: " + another_name)
print("Here's " + another_name + " written the the cases swapped: " + another_name.swapcase())

A = 10
if A != 5:
    print("A is not equal to 5.")

name = "Carl"
if name == "Stanley":
    print("Hello, Stanley")
else:
    print("You are not Stanley")

answer = "Yellow"
if answer == "Red":
    print("You chose red.")
elif answer == "Blue":
    print("You chose blue.")
else:
    print("Please enter Red or Blue as your answer.")

Best_bands_list = ["The Beatles", "Rolling Stones", "Led Zepplin", "Beach Boys"]
print(Best_bands_list[0] + " is an awesome band!")
Best_bands_list.append("The Temptations")
print(Best_bands_list)
Best_bands_list[2] = "The Supremes"
print(Best_bands_list)

List_of_numbers = [5, 10, 15, 20, 25]
for numbers in List_of_numbers:
    print(numbers ** 10)

import time
Values_list = []
Values_list.append(numbers ** 10)
print(Values_list)

Birthday_Dictionary = {'Emily' : 'January 1984', 'Maxine' : 'July 1985', 'Kelly' : 'May 1955', 'Violet' : 'July 2008'}
print(Birthday_Dictionary)    
print(Birthday_Dictionary['Maxine'])
Birthday_Dictionary['Emily'] = 'March 1983'
print(Birthday_Dictionary)
print("Kelly's Birthday is: " + Birthday_Dictionary['Kelly'])
Birthday_Dictionary['Magnus'] = 'March 2018'
print(Birthday_Dictionary)
del Birthday_Dictionary['Kelly']
print(Birthday_Dictionary)

def Subtraction(A, B):
    subtract = A - B
    return subtract
print(Subtraction(20, 10))
print(Subtraction(10, 5))
print(Subtraction(500, 350))
def addition(C, D, E):
    add = C + D + E
    return add
print(addition(5, 10, 20))
def multiplication(F, G, H):
    multiply = F * G * H
    return multiply
print(multiplication(2, 4, 6))
def division(I, J, K):
    divide = I / J // K
    return divide
print(division(20, 4, 2))

X = 500
print(str(X))

K = float(699)
print(K)

How_many_characters = len("I am learning a lot from this Python course!")
print(How_many_characters)

Z = 219.67
print(Z)
Whole_number_Z = int(Z)
print(Whole_number_Z)

X = 29.76521
print(round(X))

import math
print(math.sqrt(64))

import random
print(random.randint(0,100))

Date = input('Please enter the date: ')
print('The date you entered is ' + Date + '.')

print('We are going to find out whether or not you like candy')
Candy = input('Do you like candy? ')
if Candy == 'Yes':
    print('You like candy!')
elif Candy == 'No':
    print('You do not like candy...')
else:
    print('Please enter Yes or No.')

