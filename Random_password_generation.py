#Generating the password based on user input
import random
import string

#Password length request from the user
while True:
    try:
        password_length = int(input("Enter the password length: "))
        if password_length < 1:
            raise ValueError("Password length must be longer 0")
        break
    except ValueError as error:
        print(f"Error: {error}")

#Requesting the use of special characters from the user
while True:
    try:
        use_special_chars = input("Use special characters? (y/n): ")
        if use_special_chars.lower() == "y":
            special_chars = string.punctuation
            break
        elif use_special_chars.lower() == "n":
            special_chars = ""
            break
        else:
            raise ValueError("Incorrect input")
    except ValueError as error:
        print(f"Error: {error}")

#Requesting the use of numbers from the user
while True:
    try:
        use_numbers = input("Use numbers? (y/n): ")
        if use_numbers.lower() == "y":
            numbers = string.digits
            break
        elif use_numbers.lower() == "n":
            numbers = ""
            break
        else:
            raise ValueError("Incorrect input")
    except ValueError as error:
        print(f"Error: {error}")

#Requesting the use of letters (upper and lower case)
## from the user
while True:
    try:
        use_letters = input("Use letters? (y/n): ")
        if use_letters.lower() == "y":
            letters = string.ascii_letters
            break
        elif use_letters.lower() == "n":
            letters = ""
            break
        else:
            raise ValueError("Incorret input")
    except ValueError as error:
        print(f"Error: {error}")


#Combining the character types requested by the user
characters = letters + numbers + special_chars

#Generating the password
password = "".join(random.choice(characters) for i in range(password_length))

#Printing the password
print(f"Generated password: {password}")