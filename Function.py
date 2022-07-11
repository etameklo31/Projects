
mySentence = 'loves the color'

color_list = ['red', 'blue', 'black', 'teal', 'yellow'] 

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Madisen':
            print('Madisen, you may not use this software!')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

def multiply(i):
    return i * i;

y = lambda x: x * x * x

print(y(20))
print(multiply(3))

def getSum(num1,num2):
    answer = num1 + num2
    print('The answer is {}.'.format(answer))
