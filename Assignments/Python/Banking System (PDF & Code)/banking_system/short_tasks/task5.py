def is_valid_password(password):
    # Check the length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    # Password is valid
    return True, "Password is valid."


print("Welcome to the Bank!")

while True:
    user_password = input("Create your password: ")
    is_valid, message = is_valid_password(user_password)

    if is_valid:
        print("Password successfully created!")
        break
    else:
        print(f"Invalid password: {message}. Please try again.")
