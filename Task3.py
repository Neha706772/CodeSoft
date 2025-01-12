#A password generator is a useful tool that generates strong and
#random passwords for users. This project aims to create apassword generator application using Python, allowing users to
#specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the
#password.Generate Password: Use a combination of random characters to
#generate a password of the specified length.
#Display the Password: Print the generated password on the screen.
import random
import string


def password_generator():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters for better security.")
            return
        print("\nChoose the complexity of your password:")
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'

        char_pool = string.ascii_lowercase  # Always include lowercase letters
        if use_uppercase:
            char_pool += string.ascii_uppercase
        if use_numbers:
            char_pool += string.digits
        if use_symbols:
            char_pool += string.punctuation

        if not char_pool:
            print("Error: No character types selected. Please choose at least one.")
            return

        password = ''.join(random.choice(char_pool) for _ in range(length))

        print("\nYour generated password is:")
        print(password)

    except ValueError:
        print("Error: Please enter a valid number for the password length.")

password_generator()
