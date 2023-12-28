from db_connector.db_adapter import get_db_connection


class Payment:

    def __init__(self, payment_id, student, amount, payment_date):
        self.connection = get_db_connection()
        self.__payment_id = payment_id
        self.__student = student
        self.__amount = amount
        self.__payment_date = payment_date

    def get_payment_id(self):
        return self.__payment_id

    def get_student(self):
        return self.__student

    def get_payment_amount(self):
        return self.__amount

    def get_payment_date(self):
        return self.__payment_date

    def display_payment_info(self):
        print('Payment ID: ', self.__payment_id)
        print('Student Details: ', self.__student)
        print('Payment Amount: ', self.__amount)
        print('Payment Date: ', self.__payment_date)
