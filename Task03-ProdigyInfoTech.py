"""TASK03-Password Complexity Checker"""
import string

# Password that the user wants to check the complexity thereof
user_password = input("Enter the password you want to be checked: ")

# Different types of methods to check password complexity
has_upper_case = any(c in string.ascii_uppercase for c in user_password)  # Check for uppercase
has_lower_case = any(c in string.ascii_lowercase for c in user_password)  # Check for lowercase
has_special_character = any(c in string.punctuation for c in user_password)    # Check for special characters
has_numerical_value = any(c in string.digits for c in user_password)           # Check for digits
password_length = len(user_password)

# Score to track password complexity of the passwords
score = 0

# Open the common password list and check if the password is in it
try:
    with open('password-list.txt', 'r') as f:
        common_passwords = f.read().splitlines()
    if user_password in common_passwords:
        print("Password is weak and already exists in the common password list. Score: 0/10")
        exit()
except FileNotFoundError:
    #incase the file is not found
    print("Warning: Common password file not found. Skipping this check.")

# Checking password length to increase score
if password_length > 8:
    score += 1
if password_length > 12:
    score += 1
if password_length > 17:
    score += 1
if password_length > 20:
    score += 1
if password_length > 25:
    score += 1

print(f"Password length is {password_length}, adding {score} points for length!")

# Character type scoring
character_types = [has_upper_case, has_lower_case, has_special_character, has_numerical_value]
character_type_count = sum(character_types)

if character_type_count > 1:
    score += 1
if character_type_count > 2:
    score += 1
if character_type_count > 3:
    score += 1

print(f"Password has {character_type_count} different character types, adding {character_type_count - 1} points!")

# Evaluate password strength
if score <= 1:
    print(f"The password is very weak. Score: {score}/8")
elif 2 <= score <= 3:
    print(f"The password is quite weak. Score: {score}/8")
elif 4 <= score <= 6:
    print(f"The password is moderate. Score: {score}/8")
else:
    print(f"The password is strong! Score: {score}/8")
