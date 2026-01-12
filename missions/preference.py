# Create preference.py. 
# Ask user: "Do you like dark environments? (yes/no)" 
# Ask user: "Do you like jokes? (yes/no)"
# If dark is "yes" AND jokes is "no": Print 
# "Welcome to the DC Universe."
# If dark is "no" AND jokes is "yes": Print 
# "Welcome to the MCU."
# Else: Print "You might like The Boys."

like_dark = input("Do you like dark environments? (yes/no)\n")
like_jokes = input("Do you like jokes? (yes/no)\n")

if like_dark == "yes" and like_jokes == "no":
    print("Welcome to the DC Universe.")
elif like_dark == "no" and like_jokes == "yes":
    print("Welcome to the MCU.")
else:
    print("You might like The Boys.")
