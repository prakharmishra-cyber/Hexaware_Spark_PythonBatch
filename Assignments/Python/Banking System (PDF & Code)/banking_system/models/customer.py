from db_connection.db_adapter import *


class Customer:

    def __init__(self, customer_id, first_name, last_name, dob, email, phone_number, address):
        self.connection = get_db_connection()
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_customer_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_customer_address(self):
        return self.__address

    def update_student_info(self, first_name=None, last_name=None, date_of_birth=None, email=None, phone_number=None, address=None):
        my_cursor = self.connection.cursor()

        if first_name:
            sql = '''
                UPDATE Customers SET first_name = %s WHERE customer_id = %s
            '''
            para = (first_name, self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__first_name = first_name

        if last_name:
            sql = '''
                UPDATE Customers SET last_name = %s WHERE customer_id = %s
            '''
            para = (last_name, self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__last_name = last_name

        if date_of_birth:
            sql = '''
                UPDATE Customers SET DOB = %s WHERE customer_id = %s
            '''
            para = (date_of_birth, self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__dob = date_of_birth

        if email:
            sql = '''
                UPDATE Customers SET email = %s WHERE customer_id = %s
            '''
            para = (email, self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__email = email

        if phone_number:
            sql = '''
                UPDATE Customers SET phone_number = %s WHERE customer_id = %s
            '''
            para = (phone_number, self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__phone_number = phone_number

        if address:
            sql = '''
                UPDATE Customers SET address = %s WHERE customer_id = %s
            '''
            para = (address, self.__customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__address = address

        print('Student Details Updated Successfully')
