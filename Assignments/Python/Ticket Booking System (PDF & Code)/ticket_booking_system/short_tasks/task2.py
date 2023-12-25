silver_price = 50
gold_price = 100
diamond_price = 150

while True:
    print("Ticket Options:")
    print("1. Silver")
    print("2. Gold")
    print("3. Diamond")
    print("Type 'Exit' to end the booking.")

    ticket_type = input("Enter the ticket type: ")

    if ticket_type.lower() == 'exit':
        print("Exiting the booking system. Thank you!")
        break

    try:
        no_of_tickets = int(input("Enter the number of tickets: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if ticket_type.lower() == 'silver':
        total_cost = silver_price * no_of_tickets
    elif ticket_type.lower() == 'gold':
        total_cost = gold_price * no_of_tickets
    elif ticket_type.lower() == 'diamond':
        total_cost = diamond_price * no_of_tickets
    else:
        print("Invalid ticket type. Please select Silver, Gold, or Diamond.")
        continue

    print(f"Total cost for {no_of_tickets} {ticket_type} ticket(s): ${total_cost}")
