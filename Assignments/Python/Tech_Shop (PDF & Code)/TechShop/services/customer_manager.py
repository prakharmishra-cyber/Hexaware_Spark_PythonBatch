import re

from custom_exceptions.custom_exceptions import CustomerNotFoundException
from models.customers import Customers
from db_connector.db_connector import get_db_connection
class CustomerManager:
    def __init__(self):
        self.connection = get_db_connection()

    def register_customer(self, first_name, last_name, email, dob, phone, num_orders, address):
        try:
            # Validating input data
            self.validate_customer_data(email)
            # Checking if the email already exists in the database
            if self.is_email_duplicate(email):
                raise ValueError("Email address is already registered.")

            cursor = self.connection.cursor()
            sql = 'SELECT * FROM Customers'
            cursor.execute(sql)
            x = list(cursor.fetchall())
            sql2 = 'INSERT INTO Customers(customer_id, first_name, last_name, email, DOB, phone_number, NumOrders, address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
            para = (len(x)+1, first_name, last_name, email, dob, phone, num_orders, address)
            cursor.execute(sql2, para)
            self.connection.commit()
            self.connection.close()
            print("Customer registration successful.")
        except Exception as e:
            print(f"Error registering customer: {e}")

    def validate_customer_data(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, email):
            raise ValueError("Invalid email address.")

    def is_email_duplicate(self, email):
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM Customers WHERE email = %s'
        para = (email,)
        cursor.execute(sql, para)
        x = len(list(cursor.fetchall()))
        if (x > 0):
            return True
        return False

    def get_customer_by_id(self, customer_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Customers WHERE customer_id = %s'''
            para = (customer_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise CustomerNotFoundException('Invalid Customer ID')
            else:
                return Customers(*x)
        except CustomerNotFoundException as cnfe:
            print('An error occurred ',cnfe)
        except Exception as e:
            print('An error occurred ',e)


# Example usage:
# customer_manager = CustomerManager()
# customer_manager.register_customer("Prakhar", "Mishra", "prakhar.mishra@example.com", '1990-05-01', "1234567890", 0,"Kanpur, UP, India")
