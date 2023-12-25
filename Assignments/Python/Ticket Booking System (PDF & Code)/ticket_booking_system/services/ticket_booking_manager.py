from db_connection.db_adapter import *
from models.event import Event


class BookingSystem:
    def __init__(self):
        self.connection = get_db_connection()

    def display_menu(self):
        print("1. Book Tickets")
        print("2. Cancel Booking")
        print("3. View Event Details")
        print("4. Exit")

    def book_tickets(self):
        num_tickets = int(input("Enter the number of tickets to book: "))
        customer_id = int(input('Enter the customer id: '))
        event_id = input('Enter the event ID')
        temp_event = self.get_event_by_id(event_id)
        try:
            temp_event.book_tickets(customer_id, num_tickets, event_id, temp_event.get_ticket_price())
            print('Ticket Booked Successfully')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_event_by_id(self, event_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * from event where event_id = %s
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            x = Event(*list(my_cursor.fetchone()))
            return x
        except Exception as e:
            print(f'An error occurred: {e}')

    def cancel_booking(self):
        event_id = input('Enter the event ID booking to cancel')
        booking_id = input("Enter the booking ID to cancel: ")
        temp_event = self.get_event_by_id(event_id)
        try:
            temp_event.cancel_booking(booking_id)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def view_event_details(self):
        event_id = input("Enter the event ID to view details: ")

        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * from event where event_id = %s
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            t = list(my_cursor.fetchone())
            x = Event(*t)
            x.display_event_details()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
