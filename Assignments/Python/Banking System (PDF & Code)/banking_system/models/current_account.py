from db_connection.db_adapter import *
from models.account import Account


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, account_id, customer_id, balance):
        super().__init__(account_id, customer_id, account_type="Current", balance=balance)
        self.__overdraft_limit = self.OVERDRAFT_LIMIT

    def withdraw(self, amount):
        if amount > super().get_balance() + self.__overdraft_limit:
            print('Withdrawal amount exceeds available balance and overdraft limit.')
            return

        try:
            my_cursor = super().connection.cursor()
            sql = '''
                UPDATE Accounts SET balance = %s WHERE account_id = %s
            '''
            para = (super().get_balance() - amount, super().get_account_id())
            my_cursor.execute(sql, para)
            super().connection.commit()
            super().update_account_details(balance=super().get_balance()-amount)
            print('Amount withdrawn successfully')
        except Exception as e:
            print(f'An error occurred: {e}')
