from models.bank import Bank


class BankApp:
    def __init__(self):
        self.bank = Bank()

    def create_account(self):
        while True:
            print("\nCreate Account Menu:")
            print("1. Enter Account Details")
            print("2. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.bank.create_account()
            elif choice == "2":
                print("Exiting Create Account Menu.")
                break
            else:
                print("Invalid choice. Please choose a valid option (1-3).")

    def main(self):
        while True:
            print("\nBank App Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                account_id = input("Enter the account ID: ")
                amount = float(input("Enter the deposit amount: "))
                self.bank.deposit(account_id, amount)
            elif choice == "3":
                account_id = input("Enter the account ID: ")
                amount = float(input("Enter the withdrawal amount: "))
                self.bank.withdraw(account_id, amount)
            elif choice == "4":
                account_id = input("Enter the account ID: ")
                temp_account = self.bank.get_account_by_id(account_id)
                print(temp_account.get_balance())
            elif choice == "5":
                from_account_id = input("Enter the source account ID: ")
                to_account_id = input("Enter the destination account ID: ")
                amount = float(input("Enter the transfer amount: "))
                self.bank.transfer(from_account_id, to_account_id, amount)
            elif choice == "6":
                account_id = input("Enter the account ID: ")
                self.bank.get_account_details(account_id)
            elif choice == "7":
                x = self.bank.list_all_account()
                print(*x, sep="\n\n")
            elif choice == "8":
                account_id = input("Enter the account ID: ")
                start_date = input("Enter Start Date: ")
                end_date = input("Enter End Date: ")
                x = self.bank.get_transactions(account_id, start_date, end_date)
                print(*x, sep="\n\n")
            elif choice == "9":
                print("Exiting Bank App. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option (1-9).")

if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()
