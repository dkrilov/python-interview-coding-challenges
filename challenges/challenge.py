# Challenge 4: Validate Password Strength
# Write a Python function `validate_password_strength` that takes a password as input and validates its strength using regular expressions. The function should check if the password meets certain criteria, such as having a minimum length, containing at least one uppercase letter, one lowercase letter, and one digit.
# Example:
# Input: validate_password_strength("Password123")
# Output: Strong password
import re

# Define a function named 'validate_password_strength' that takes one parameter called 'password'
def validate_password_strength(password):
    # Check if password has at least 8 characters (length requirement)
    if len(password) < 8:
        print("Weak password: Password must be at least 8 characters long")
        return
    
    # Check if password contains at least one lowercase letter using regex pattern [a-z]
    # [a-z] means any single character from 'a' to 'z' (lowercase letters only)
    if not re.search(r"[a-z]", password):
        print("Weak password: Password must contain at least one lowercase letter")
        return
    
    # Check if password contains at least one uppercase letter using regex pattern [A-Z]
    # [A-Z] means any single character from 'A' to 'Z' (uppercase letters only)
    if not re.search(r"[A-Z]", password):
        print("Weak password: Password must contain at least one uppercase letter")
        return
    
    # Check if password contains at least one digit using regex pattern \d
    # \d means any single digit character (0-9)
    if not re.search(r"\d", password):
        print("Weak password: Password must contain at least one digit")
        return
    
    # Check if password contains at least one special character using regex pattern [!@#$%^&*(),.?":{}|<>]
    # This pattern matches any single character that is in the specified set
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Weak password: Password must contain at least one special character")
        return
    
    print("Strong password")

# Test
validate_password_strength("Password123")