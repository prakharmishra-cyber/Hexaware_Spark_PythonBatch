from db_connection.db_adapter import *
from models.event import Event


class Booking:
    def __init__(self, booking_id, customer_id, event_id, num_tickets, total_cost, booking_date):
        self.connection = get_db_connection()
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.event_id = event_id
        self.num_tickets = num_tickets
        self.total_cost = total_cost
        self.booking_date = booking_date

    def get_booking_id(self):
        return self.booking_id

    def get_customer_id(self):
        return self.customer_id

    def get_event_id(self):
        return self.event_id

    def get_num_tickets(self):
        return self.num_tickets

    def get_total_cost(self):
        return self.total_cost

    def get_booking_date(self):
        return self.booking_date

    def calculate_booking_cost(self, num_tickets, event_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT total_price from event where event_id = %s
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            x = int(list(my_cursor.fetchone())[0])
            return x*num_tickets
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_available_no_of_tickets(self, event_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT available_seats from event where event_id = %s
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            x = list(my_cursor.fetchone())[0]
            return x
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_event_details(self, event_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * from event where event_id = %s
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            x = Event(*list(my_cursor.fetchone()))
            x.display_event_details()
        except Exception as e:
            print(f'An error occurred: {e}')

    def update_booking_info(self, num_tickets=None, total_cost=None, booking_date=None):
        my_cursor = self.connection.cursor()

        if num_tickets:
            sql = 'UPDATE booking SET num_tickets = %s WHERE booking_id = %s'
            para = (num_tickets, self.booking_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Number of Tickets Updated successfully')

        if total_cost:
            sql = 'UPDATE booking SET total_cost = %s WHERE booking_id = %s'
            para = (total_cost, self.booking_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Total Cost Updated successfully')

        if booking_date:
            sql = 'UPDATE booking SET booking_date = %s WHERE booking_id = %s'
            para = (booking_date, self.booking_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Booking Date Updated successfully')

        print('Booking details updated successfully')
