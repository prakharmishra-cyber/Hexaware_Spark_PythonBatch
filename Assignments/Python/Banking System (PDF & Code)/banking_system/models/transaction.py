from db_connection.db_adapter import *


class Transaction:

    def __init__(self, transaction_id, account_id, transaction_type, amount, transaction_date):
        self.connection = get_db_connection()
        self.__transaction_id = transaction_id
        self.__account_id = account_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__transaction_date = transaction_date

    def __str__(self):
        return f"Transaction ID: {self.__transaction_id}\n" \
               f"Account ID: {self.__account_id}\n" \
               f"Transaction Type: {self.__transaction_type}\n" \
               f"Amount: ${self.__amount:.2f}\n" \
               f"Transaction Date: {self.__transaction_date}"

    def get_transaction_id(self):
        return self.__transaction_id

    def get_account_id(self):
        return self.__account_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_transaction_date(self):
        return self.__transaction_date

    def get_transaction_amount(self):
        return self.__amount

    def update_transaction_info(self, account_id=None, transaction_type=None, transaction_amount=None,
                                transaction_date=None):

        my_cursor = self.connection.cursor()

        if account_id:
            try:
                sql = '''
                                UPDATE Transactions SET account_id = %s WHERE transaction_id = %s
                            '''
                para = (account_id, self.__transaction_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Account id updated successfully')
            except Exception as e:
                print(f'An error occurred: {e}')

        if transaction_type:
            try:
                sql = '''
                                UPDATE Transactions SET transaction_type = %s WHERE transaction_id = %s
                            '''
                para = (transaction_type, self.__transaction_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Transaction type updated successfully')
            except Exception as e:
                print(f'An error occurred: {e}')

        if transaction_amount:
            try:
                sql = '''
                                UPDATE Transactions SET amount = %s WHERE transaction_id = %s
                            '''
                para = (transaction_amount, self.__transaction_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Transaction Amount updated successfully')
            except Exception as e:
                print(f'An error occurred: {e}')

        if transaction_date:
            try:
                sql = '''
                                UPDATE Transactions SET transaction_date = %s WHERE transaction_id = %s
                            '''
                para = (transaction_date, self.__transaction_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Transaction date updated successfully')
            except Exception as e:
                print(f'An error occurred: {e}')
