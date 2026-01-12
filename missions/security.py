# Create security.py. 
# Define a password variable (e.g., "Mark42"). 
# Ask the user for input: "Enter password: ". 
# If it matches, print "Access Granted. Welcome, Tony." 
# Else, print "Access Denied. Activating Defense Protocol."

current_password = "Mark42"

typed_password = input("Enter password: ")

if current_password == typed_password:
    print("Access Granted. Welcome, Tony.")
else:
    print("Access Denied. Activating Defense Protocol.")


