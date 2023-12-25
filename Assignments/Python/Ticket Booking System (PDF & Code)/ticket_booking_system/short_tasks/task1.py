available_tickets = int(input("Enter the number of available tickets: "))
no_of_booking_tickets = int(input("Enter the number of tickets to book: "))


if available_tickets >= no_of_booking_tickets:
    remaining_tickets = available_tickets - no_of_booking_tickets
    print(f"Tickets booked successfully! Remaining tickets: {remaining_tickets}")
else:
    print("Sorry, tickets unavailable. Please try again with a smaller quantity.")
