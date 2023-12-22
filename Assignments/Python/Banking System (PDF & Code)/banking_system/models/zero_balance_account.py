from db_connection.db_adapter import *
from models.account import Account


class ZeroBalanceAccount(Account):

    def __init__(self, account_id, customer_id, account_type):
        self.connection = get_db_connection()
        super().__init__(account_id, customer_id, account_type, 0)
