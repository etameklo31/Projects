
#Parent Class User
class User:
    name = 'Jim'
    email = 'jim@gmail.com'
    password = '9876abcd'
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('The password or email is  incorrect.')

#Child Class Employee
class Employee(User):
    base_pay = 15.00
    department = "IT"
    pin_number = '3980'

class Employee_2(User):
    benefits =  'Health and Dental'
    department = 'HR'
    HR email = 'hr@gmail.com'

#This is the same method in the parent class 'User'.
#The difference is that, intstead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        entry_pin = input('Enter your pin: ')
        if (entry_email == self.email and entry_pin == self.pin_number):
            print('Welccome back, {}!'.format(entry_name))
        else:
            print('The pin or email is incorrect')

#The following code invokes the methods inside each class for User and Employee.

if __name__ == '__main__':
    customer = User()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLoginInfo()

    manager2 = Employee_2()
    manager2.getLoginInfo()
