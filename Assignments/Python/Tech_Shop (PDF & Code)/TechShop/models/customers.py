from db_connector.db_connector import get_db_connection
class Customers:
    def __init__(self, customer_id, first_name, last_name, email, dob, phone, num_orders, address):
        self.connection = get_db_connection()
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__dob = dob
        self.__phone = phone
        self.__num_orders = num_orders
        self.__address = address

    def calculate_total_orders(self):
        cursor = self.connection.cursor()
        sql = 'select %s, Count(*) AS No_Of_Orders from orders where CustomerID = %s;'
        para = (self.__customer_id, self.__customer_id)
        cursor.execute(sql, para)
        temp = list(cursor.fetchone())
        return temp[1]

    def get_customer_details(self):
        details = f"Customer ID: {self.__customer_id}\n"
        details += f"Name: {self.__first_name} {self.__last_name}\n"
        details += f"DOB: {self.__dob}\n"
        details += f"Email: {self.__email}\n"
        details += f"Phone: {self.__phone}\n"
        details += f"Address: {self.__address}\n"
        return details

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            cursor = self.connection.cursor()
            sql = 'UPDATE Customers SET email = %s WHERE customer_id = %s'
            para = (email, self.__customer_id)
            cursor.execute(sql, para)
            self.__email = email
        if phone:
            cursor = self.connection.cursor()
            sql = 'UPDATE Customers SET phone = %s WHERE customer_id = %s'
            para = (phone, self.__customer_id)
            cursor.execute(sql, para)
            self.__phone = phone
        if address:
            cursor = self.connection.cursor()
            sql = 'UPDATE Customers SET address = %s WHERE customer_id = %s'
            para = (address, self.__customer_id)
            cursor.execute(sql, para)
            self.__address = address

    def get_num_orders(self):
        return self.__num_orders

    # Getter for customer_id
    def get_customer_id(self):
        return self.__customer_id

    # Getter for first_name
    def get_first_name(self):
        return self.__first_name

    # Getter for last_name
    def get_last_name(self):
        return self.__last_name

    # Getter for email
    def get_email(self):
        return self.__email

    # Getter for phone
    def get_phone(self):
        return self.__phone

    # Getter for address
    def get_address(self):
        return self.__address

    def get_dob(self):
        return self.__dob



