# Helps us know date & time
from datetime import *
print(datetime.now())

# geather user name
def name():
    n = input("Enter Name: ")
name()

# connection for storing user name
from user_storage import set_user_name, get_user_name

# Example usage
user_id = "user_1"

# Set user name
response = set_user_name(user_id, "Shubham")
print(response)  # Output: Name updated to Shubham!

# Get user name
name = get_user_name(user_id)
print(name)  # Output: Shubham
