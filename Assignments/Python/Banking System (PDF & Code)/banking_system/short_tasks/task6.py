def display_transaction_history(transaction_history):
    print("\nTransaction History:")
    for transaction in transaction_history:
        print(transaction)

# Main program

print("Welcome to the Bank!")
transaction_history = []

while True:
    transaction_type = input("Enter transaction type (deposit/withdrawal) or 'exit' to finish: ")

    if transaction_type.lower() == 'exit':
        break

    try:
        amount = float(input("Enter transaction amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        continue

    if transaction_type.lower() == 'deposit':
        transaction_history.append(f"Deposit: +${amount:.2f}")
    elif transaction_type.lower() == 'withdrawal':
        transaction_history.append(f"Withdrawal: -${amount:.2f}")
    else:
        print("Invalid transaction type. Please enter 'deposit', 'withdrawal', or 'exit'.")

display_transaction_history(transaction_history)
print("Thank you for using the Bank. Goodbye!")
