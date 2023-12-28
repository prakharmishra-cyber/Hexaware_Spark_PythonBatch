from db_connection.db_adapter import *
from models.account import Account
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.transaction import Transaction


class Bank:

    def __init__(self):
        self.connection = get_db_connection()

    def deposit(self, account_id, amount):
        my_cursor = self.connection.cursor()
        try:
            sql = '''
                UPDATE Accounts SET balance = balance + %s WHERE account_id = %s
            '''
            para = (amount, account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Amount deposited successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def withdraw(self, account_id, amount):
        my_cursor = self.connection.cursor()
        try:
            sql = '''
                UPDATE Accounts SET balance = balance - %s WHERE account_id = %s
            '''
            para = (amount, account_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Amount withdrawn successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_account_by_id(self, account_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Accounts WHERE account_id = %s
            '''
            para = (account_id,)
            my_cursor.execute(sql, para)
            x = Account(*list(my_cursor.fetchone()))
            return x
        except Exception as e:
            print(f'An error occurred: {e}')

    def calculate_interest(self, account_id):
        try:
            customer_account = self.get_account_by_id(account_id)
            value = customer_account.calculate_interest()
            customer_account.update_account_details(balance=value)
        except Exception as e:
            print(f'An error occurred: {e}')

    def create_customer_account(self, account):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                INSERT INTO Accounts(account_id, customer_id, account_type, balance)
                VALUES (%s, %s, %s, %s)
            '''
            para = (account.get_account_id(), account.get_customer_id(), account.get_account_type(), account.get_balance())
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Account created successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def create_account(self):
        print("Choose the type of account:")
        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Enter your choice (1 or 2): ")

        # account_id = input("Enter the account ID: ")
        customer_id = input("Enter the customer ID: ")
        initial_balance = float(input("Enter the initial balance: "))

        if choice == "1":
            interest_rate = float(input("Enter the interest rate for Savings Account: "))
            account = SavingsAccount(get_ids('accounts', 'account_id'), customer_id, initial_balance, interest_rate)
            self.create_customer_account(account)
        elif choice == "2":
            account = CurrentAccount(get_ids('accounts', 'account_id'), customer_id, initial_balance)
            self.create_customer_account(account)
        else:
            print("Invalid choice. Please choose 1 or 2.")
            return

        print("Account created successfully!")
        print("Account details:")
        account.print_account_info()

    def get_account_balance_by_id(self, account_id):
        try:
            customer_account = self.get_account_by_id(account_id)
            return customer_account.get_balance()
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_account_details(self, account_id):
        try:
            customer_account = self.get_account_by_id(account_id)
            customer_account.print_account_info()
        except Exception as e:
            print(f'An error occurred: {e}')

    def transfer(self, sender_account_id, receiver_account_id, amount):
        try:
            sender_account = self.get_account_by_id(sender_account_id)
            receiver_account = self.get_account_by_id(receiver_account_id)

            if sender_account.get_balance()<amount:
                print('Insufficient balance in sender account')
            else:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
                print('Transaction made successfully')

        except Exception as e:
            print(f'An error occurred: {e}')

    def get_transactions(self, account_id, start_date, end_date):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Transactions WHERE account_id = %s AND
                transaction_date BETWEEN %s AND %s
            '''
            para = (account_id, start_date, end_date)
            my_cursor.execute(sql, para)
            x = [Transaction(*list(i)) for i in list(my_cursor.fetchall())]
            return x
        except Exception as e:
            print(f'An error occurred: {e}')

    def list_all_account(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Accounts
            '''
            my_cursor.execute(sql)
            x = [Account(*list(i)) for i in list(my_cursor.fetchall())]
            return x
        except Exception as e:
            print(f'An error occurred: {e}')



