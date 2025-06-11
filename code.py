# password-generator
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        return "Error: No character sets selected."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage:
length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

print("\nGenerated Password:", generate_password(length, use_upper, use_lower, use_digits, use_special))

