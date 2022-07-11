class User:
    name = 'No Name Provided'
    email = ' '
    password = 'abcd1234'
    account_number = 0

class Employee(User):
    base_pay = 14.00
    department = 'HR'

class Customer(User):
    mailing_address = ' '
    mailing_list = True

if __name__ == '__main__':
    
