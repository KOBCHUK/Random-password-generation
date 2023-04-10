
import random
import string

def generate_password(length, use_special_chars, use_digits, use_letters):
    characters = ""
    if use_special_chars:
        characters += string.punctuation
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    password = "".join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
use_special_chars = input("Use special characters? (y/n): ").lower() == "y"
use_digits = input("Use digits? (y/n): ").lower() == "y"
use_letters = input("Use letters? (y/n): ").lower() == "y"

password = generate_password(length, use_special_chars, use_digits, use_letters)
print(f"Generated password: {password}")