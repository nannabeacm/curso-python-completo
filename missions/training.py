# Create training.py. 
# Ask the user: "How many laps?" (e.g., 5). 
# Use a for loop to print: "Running lap 1..." 
# "Running lap 2..." ... "Running lap 5..." "On your left!"

laps = int(input("How many laps? "))

for i in range(laps):
    print(f"Runnning lap {i+1}...")

print("On your left!")
