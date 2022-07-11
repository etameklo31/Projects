from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print('Your purchase amount: ',amount)
#this function is telling us how to pass an arguement, but we wont tell you how or what kind of data it will be
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
#there we've defined how to implement the payment function from its parent payslip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
