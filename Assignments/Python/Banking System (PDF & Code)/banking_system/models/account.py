from db_connection.db_adapter import *


class Account:

    def __init__(self, account_id, customer_id, account_type, balance):
        self.connection = get_db_connection()
        self.__account_id = account_id
        self.__customer_id = customer_id
        self.__account_type = account_type
        self.__balance = balance

    def __str__(self):
        return f"Account ID: {self.__account_id}\n" \
               f"Customer ID: {self.__customer_id}\n" \
               f"Account Type: {self.__account_type}\n" \
               f"Balance: ${self.__balance:.2f}"

    def get_account_id(self):
        return self.__account_id

    def get_customer_id(self):
        return self.__customer_id

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def update_account_details(self, account_type=None, balance=None):
        my_cursor = self.connection.cursor()

        if account_type:
            sql = '''
            UPDATE Accounts SET account_type = %s WHERE account_id = %s
            '''
            para = (account_type, self.__account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__account_type = account_type
            print('Account Type updated successfully')

        if balance:
            sql = '''
            UPDATE Accounts SET balance = %s WHERE account_id = %s
            '''
            para = (balance, self.__account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__balance = balance
            print('Account Type updated successfully')

    def deposit(self, amount):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                     UPDATE Accounts SET balance = %s WHERE account_id = %s
                    '''
            para = (self.__balance + amount, self.__account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__balance += amount
            print('Amount deposited successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient balance')
            return
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                     UPDATE Accounts SET balance = %s WHERE account_id = %s
                    '''
            para = (self.__balance - amount, self.__account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__balance -= amount
            print('Amount withdrawn successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def calculate_interest(self):
        print(f'Amount after interest: ${self.__balance + (self.__balance * 0.45)}')
        return self.__balance + (self.__balance * 0.45)

    def print_account_info(self):
        print('Account ID:', self.__account_id)
        print('Account Type:', self.__account_type)
        print('Account Balance:', self.__balance)