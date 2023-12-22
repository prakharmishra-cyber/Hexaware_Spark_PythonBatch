'''
Create a program that simulates an ATM transaction. Display options such as "Check Balance,"
"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to
withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the
available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate
messages for success or failure.
'''


class Account:

    def __init__(self, balance=0):
        self.balance = balance

    def withdrawal(self, amount):
        if amount > self.balance:
            print('Amount requested is greater than available balance')
        elif not amount % 100 == 0:
            print('Amount should be multiple of 100 or 500')
        else:
            self.balance -= amount
            print('Withdrawal Successful')

    def deposit(self, amount):
        print('Deposit made successfully')
        self.balance += amount

    def check_balance(self):
        print(self.balance)


a1 = Account(1000)
a1.check_balance()
a1.withdrawal(440)
a1.deposit(3000)
a1.check_balance()
