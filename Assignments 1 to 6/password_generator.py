import random
import string

def create_password(size):
    allowed_chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choices(allowed_chars, k=size))

print("=== SecurePass Creator ===")

try:
    user_length = int(input("How long should your password be? "))
    if user_length <= 0:
        print("Password length must be greater than 0.")
    else:
        new_password = create_password(user_length)
        print(f"🔐 Your new secure password: {new_password}")
except ValueError:
    print("Please enter a valid number.")
