bank_accounts = {
    '123456': 1500.50,
    '789012': 3000.25,
    '345678': 500.75,
}

# Function to validate the account number
def is_valid_account(account_number):
    return account_number in bank_accounts

# Function to get user input for account number
def get_account_number():
    while True:
        account_number = input("Enter your account number: ")
        if is_valid_account(account_number):
            return account_number
        else:
            print("Invalid account number. Please try again.")

# Function to display the account balance
def display_balance(account_number):
    balance = bank_accounts[account_number]
    print(f"Account Number: {account_number}\nBalance: ${balance:.2f}")


print("Welcome to the Bank!")

# Loop to repeatedly ask for the user's account number
while True:
    account_number = get_account_number()
    display_balance(account_number)

    # Ask if the user wants to check another account
    another_account = input("Do you want to check another account? (yes/no): ")
    if another_account.lower() != 'yes':
        print("Thank you for using the Bank. Goodbye!")
        break
