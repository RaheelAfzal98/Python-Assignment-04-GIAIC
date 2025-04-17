# Problem Statement
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!
# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
# For example, using a hash function called SHA256(...) something as simple as
# hello
# can be hashed into a much more complex
# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.
# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)



import hashlib

def verify_credentials(user_email, login_data, input_password):
    """
    Checks if the provided password matches the hashed password stored in login_data for the user_email.
    
    Parameters:
        user_email (str): The email of the user trying to log in.
        login_data (dict): Dictionary with email-passwordHash pairs.
        input_password (str): The password entered by the user.
    
    Returns:
        bool: True if the password is correct, otherwise False.
    """
    hashed_input = generate_hash(input_password)
    return login_data.get(user_email) == hashed_input


def generate_hash(text):
    """
    Converts a given text into a SHA256 hash string.
    
    Parameters:
        text (str): The text to hash.
    
    Returns:
        str: The SHA256 hash of the input.
    """
    return hashlib.sha256(text.encode()).hexdigest()


def run_checks():
    # Simulated hashed login information
    login_data = {
        "example@gmail.com": generate_hash("password"),
        "code_in_placer@cip.org": generate_hash("karel"),
        "student@stanford.edu": generate_hash("123!456?789")
    }

    # Checking credentials
    print(verify_credentials("example@gmail.com", login_data, "word"))          # False
    print(verify_credentials("example@gmail.com", login_data, "password"))      # True

    print(verify_credentials("code_in_placer@cip.org", login_data, "Karel"))    # False
    print(verify_credentials("code_in_placer@cip.org", login_data, "karel"))    # True

    print(verify_credentials("student@stanford.edu", login_data, "password"))   # False
    print(verify_credentials("student@stanford.edu", login_data, "123!456?789"))# True


if __name__ == "__main__":
    run_checks()
