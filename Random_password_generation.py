import random
import string

while True:
    try:
        password_length = int(input("Enter password length: "))
        if password_length < 1:
            raise ValueError("Password length must be longer 0")
        break
    except ValueError as error:
        print(f"Error: {error}")


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
            raise ValueError("Incorrect input")
    except ValueError as error:
        print(f"Error: {error}")


all_chars = special_chars + numbers + letters


password = "".join(random.choices(all_chars, k=password_length))

print(f"Generated password: {password}")
