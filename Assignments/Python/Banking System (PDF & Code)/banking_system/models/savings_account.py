from db_connection.db_adapter import *
from models.account import Account


class SavingsAccount(Account):
    def __init__(self, account_id, customer_id, balance, interest_rate):
        super().__init__(account_id, customer_id, account_type="Savings", balance=balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = super().get_balance() * (self.__interest_rate / 100)
        print(f'Interest calculated for Savings Account: ${interest_amount:.2f}')
        return super().get_balance() + interest_amount
