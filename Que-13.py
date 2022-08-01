# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

password = input("Enter your password:")
spchar = ['@','$','#']
flag=0
if(len(password)<6):
    print("minimum length should be 6")
    flag=1
if(len(password)>16):
    print("maximum length should be 16")
    flag=1
if not any(char.isdigit() for char in password):
    print("at least 1 digit is required")
    flag=1
if not any(char.isupper() for char in password):
    print("at least 1 upper case character is required")
    flag=1
if not any(char.islower() for char in password):
    print("at least 1 lower case character is required")
    flag=1
if not any(char in spchar for char in password):
    print("at least 1 special character is required")
    flag=1
if(flag==0):
    print("Password matches all the requirments")
