# Function to calculate future balance
def calculate_future_balance(initial_balance, annual_interest_rate, years):
    future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
    return future_balance


# Function to get user input for multiple customers
def get_user_input():
    customers = []

    num_customers = int(input("Enter the number of customers: "))

    for i in range(num_customers):
        print(f"\nCustomer {i + 1}:")
        initial_balance = float(input("Enter the initial balance: "))
        annual_interest_rate = float(input("Enter the annual interest rate (%): "))
        years = int(input("Enter the number of years: "))

        customers.append({
            'initial_balance': initial_balance,
            'annual_interest_rate': annual_interest_rate,
            'years': years
        })

    return customers


# Function to display future balance for each customer
def display_future_balances(customers):
    print("\nFuture Balances:")
    for i, customer in enumerate(customers, start=1):
        future_balance = calculate_future_balance(customer['initial_balance'],
                                                  customer['annual_interest_rate'],
                                                  customer['years'])
        print(f"Customer {i}: ${future_balance:.2f}")


customer_data = get_user_input()
display_future_balances(customer_data)
