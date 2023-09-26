def is_valid_password(password):
	if len(password) >= 8:
		return True
	else:
		return False

# Get user input for the password
user_password = input("Enter a password: ")

# Check if the password is valid 
if is_valid_password(user_password):
	print("Password is valid")
else:
	print("Password is to short. It must be at least 8 characters long.")
