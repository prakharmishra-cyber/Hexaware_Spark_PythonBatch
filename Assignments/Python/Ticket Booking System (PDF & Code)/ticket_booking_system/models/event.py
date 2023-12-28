from datetime import date

from db_connection.db_adapter import *

class Event:
    def __init__(self, event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, booking_id):
        self.connection = get_db_connection()
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.booking_id = booking_id

    def get_event_id(self):
        return self.event_id

    def get_event_name(self):
        return self.event_name

    def get_event_date(self):
        return self.event_date

    def get_event_time(self):
        return self.event_time

    def get_venue_id(self):
        return self.venue_id

    def get_total_seats(self):
        return self.total_seats

    def get_available_seats(self):
        return self.available_seats

    def get_ticket_price(self):
        return self.ticket_price

    def get_event_type(self):
        return self.event_type

    def get_booking_id(self):
        return self.booking_id

    def calculate_total_revenue(self):
        return self.ticket_price*(self.total_seats-self.available_seats)

    def get_booked_no_of_tickets(self):
        return self.total_seats-self.available_seats

    def book_tickets(self, customer_id, num_tickets, event_id, ticket_price):
        if num_tickets>self.available_seats:
            print('Insufficient available seats')
            return
        try:
            my_cursor = self.connection.cursor()
            sql1 = '''
            INSERT INTO booking(booking_id, customer_id, event_id, num_tickets, total_cost, booking_date)
            VALUES(%s, %s, %s, %s, %s, %s)
            '''
            para1 = (get_ids('booking', 'booking_id'), customer_id, event_id, num_tickets, num_tickets*ticket_price, date.today())
            my_cursor.execute(sql1, para1)
            sql2 = '''
            UPDATE event SET available_seats = available_seats - %s WHERE event_id = %s'''
            para2 = (num_tickets, event_id)
            my_cursor.execute(sql2, para2)
            self.update_event_info(available_seats=self.available_seats-num_tickets)
            self.connection.commit()
            print('Ticket Booked successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def cancel_booking(self, booking_id):
        try:
            my_cursor = self.connection.cursor()
            my_cursor.callproc('cancel_booking', [booking_id])
            self.connection.commit()
            print('Ticket Cancelled successfully')
        except Exception as e:
            print(f'An error occurred: {e}')


    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue ID: {self.venue_id}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")
        print(f'Booking ID: {self.booking_id}')

    def update_event_info(self, event_name=None, event_date=None, event_time=None, venue_id=None,
                          total_seats=None, available_seats=None, ticket_price=None, event_type=None):
        my_cursor = self.connection.cursor()

        if event_name:
            sql = 'UPDATE event SET Event_Name = %s WHERE event_id = %s'
            para = (event_name, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Event Name Updated successfully')

        if event_date:
            sql = 'UPDATE event SET Event_Date = %s WHERE event_id = %s'
            para = (event_date, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Event Date Updated successfully')

        if event_time:
            sql = 'UPDATE event SET Event_Time = %s WHERE event_id = %s'
            para = (event_time, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Event Time Updated successfully')

        if venue_id:
            sql = 'UPDATE event SET Venue_id = %s WHERE event_id = %s'
            para = (venue_id, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Venue IF Updated successfully')

        if total_seats:
            sql = 'UPDATE event SET Total_Seats = %s WHERE event_id = %s'
            para = (total_seats, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Total Seats Updated successfully')

        if available_seats:
            sql = 'UPDATE event SET Available_Seats = %s WHERE event_id = %s'
            para = (available_seats, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Available Seats Updated successfully')

        if ticket_price:
            sql = 'UPDATE event SET Ticket_Price = %s WHERE event_id = %s'
            para = (ticket_price, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Ticket Price Updated successfully')

        if event_type:
            sql = 'UPDATE event SET Event_Type = %s WHERE event_id = %s'
            para = (event_type, self.event_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Event Type Updated successfully')

        print('Event details updated successfully')
