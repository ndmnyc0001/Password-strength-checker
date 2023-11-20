import re

def check_password_strength(password):
    # Define each criterion for a strong password
    # First criterion is having a password that is 8 characters long
    length_criteria = len(password) >= 8

    # Password should have at least one uppercase letter
    uppercase_criteria = any(char.isupper() for char in password)

    # Password should have at least one lowercase letter
    lowercase_criteria = any(char.islower() for char in password)

    # Password should also have numbers
    number_criteria = any(char.isdigit() for char in password)

    # Password must contain symbols
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Making sure that the password being created is meeting the requirements
    if all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]):
        return "Strong password"
    else:
        return "Weak password"

# Example usage
password_input = input("Enter your password: ")
result = check_password_strength(password_input)
print(result)
