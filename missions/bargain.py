# Create bargain.py. Create a variable bargain_count = 0. 
# Start a while loop that runs as long as bargain_count is less than 5.
#  Inside the loop: Print "Dormammu, I've come to bargain."
# Ask user input: "Does Dormammu accept? (yes/no)"
# If user types "yes": print "Universe Saved!" and break.
# Else: increase bargain_count by 1.
# If the loop finishes without a "yes" (after 5 tries), print "Dormammu wins...".

bargain_count = 0
bargain_limit = 10

while bargain_count < bargain_limit:
    print("Dormammu, I've come to bargain.")
    answer = input("Does Dormammu accept? (yes/no)\n")
    if answer == "yes":
        print("Universe saved!")
        break
    else:
        bargain_count = bargain_count + 1

if bargain_count == bargain_limit: 
    print("Dormammu wins...")

