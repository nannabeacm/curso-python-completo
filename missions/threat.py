# Create threat.py. Ask for the number of aliens invading (integer input).
# If less than 10: "Spider-Man can handle this."
# If between 10 and 50 (inclusive): "Call the Avengers."
# If more than 50: "Call Captain Marvel.

number_aliens = int(input("How many aliens are invading NY?\n"))

if number_aliens < 10: 
    print("Spider-Man can handle this.")
elif number_aliens >= 10 and number_aliens <= 50:
    print("Call the Avengers.")
else:
    print("Call Captain Marvel.")