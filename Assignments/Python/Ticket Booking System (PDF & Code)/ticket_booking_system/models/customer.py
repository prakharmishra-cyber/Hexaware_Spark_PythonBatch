from db_connection.db_adapter import *

class Customer:
    def __init__(self, customer_id, customer_name, email, phone_number, booking_id):
        self.connection = get_db_connection()
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.booking_id = booking_id

    # Getter and setter methods
    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_booking_id(self):
        return self.booking_id

    def display_customer_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Booking ID: {self.booking_id}")

    def update_customer_info(self, customer_name=None, email=None, phone_number=None, booking_id=None):
        my_cursor = self.connection.cursor()

        if customer_name:
            sql = 'UPDATE customer SET Customer_Name = %s WHERE customer_id = %s'
            para = (customer_name, self.customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Customer Name Updated successfully')

        if email:
            sql = 'UPDATE customer SET Email = %s WHERE customer_id = %s'
            para = (email, self.customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Email Updated successfully')

        if phone_number:
            sql = 'UPDATE customer SET Phone_Number = %s WHERE customer_id = %s'
            para = (phone_number, self.customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Phone Number Updated successfully')

        if booking_id:
            sql = 'UPDATE customer SET booking_id = %s WHERE customer_id = %s'
            para = (booking_id, self.customer_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Booking ID Updated successfully')

        print('Customer details updated successfully')
