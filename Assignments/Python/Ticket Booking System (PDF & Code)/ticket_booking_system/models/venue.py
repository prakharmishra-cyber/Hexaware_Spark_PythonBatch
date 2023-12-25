from db_connection.db_adapter import *


class Venue:
    def __init__(self, venue_id, venue_name, address):
        self.connection = get_db_connection()
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.address = address

    def get_venue_id(self):
        return self.venue_id

    def get_venue_name(self):
        return self.venue_name

    def get_address(self):
        return self.address

    def display_venue_details(self):
        print(f"Venue ID: {self.venue_id}")
        print(f"Venue Name: {self.venue_name}")
        print(f"Address: {self.address}")

    def update_venue_info(self, venue_name=None, address=None):
        my_cursor = self.connection.cursor()

        if venue_name:
            sql = 'UPDATE venue SET Venue_Name = %s WHERE venue_id = %s'
            para = (venue_name, self.venue_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Venue Name Updated successfully')

        if address:
            sql = 'UPDATE venue SET Address = %s WHERE venue_id = %s'
            para = (address, self.venue_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Address Updated successfully')

        print('Venue details updated successfully')
