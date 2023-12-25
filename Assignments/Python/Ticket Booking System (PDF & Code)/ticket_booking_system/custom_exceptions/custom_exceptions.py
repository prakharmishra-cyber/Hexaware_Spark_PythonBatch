class EventNotFoundException(Exception):
    def __init__(self, event_id):
        self.event_id = event_id
        self.message = f"Event with ID '{event_id}' not found in the menu."

class InvalidBookingIDException(Exception):
    def __init__(self, booking_id):
        self.booking_id = booking_id
        self.message = f"Invalid booking ID '{booking_id}'. Booking not found."