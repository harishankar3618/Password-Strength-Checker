import re

def check_password_strength(password):
    # Define criteria
    length = len(password) >= 8
    lowercase = any(c.islower() for c in password)
    uppercase = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in '!@#$%^&*()-_+=[]{}|\\:;"\'<>,.?/~`' for c in password)

    # Calculate score
    score = sum([length, lowercase, uppercase, digit, special_char])

    # Feedback
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    elif score >= 1:
        return "Weak"
    else:
        return "Very Weak"


def main():
    print("Welcome to the Password Strength Checker!")
    print("Please enter a password to assess its strength.")

    while True:
        password = input("Password: ")
        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        strength = check_password_strength(password)
        print("Password strength:", strength)

        choice = input("Do you want to check another password? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the Password Strength Checker")
            break


if __name__ == "__main__":
    main()
