from services.ticket_booking_manager import *

if __name__ == "__main__":
    booking_system = BookingSystem()

    while True:
        booking_system.display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            booking_system.book_tickets()

        elif choice == "2":
            booking_system.cancel_booking()

        elif choice == "3":
            booking_system.view_event_details()

        elif choice == "4":
            print("Exiting the Booking System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")