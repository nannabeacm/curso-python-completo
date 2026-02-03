### 91
print("\n===== 91 ======\n")

inventory = {}
asking = True

while asking:
    ask_user = input("Do you wish to view inventory, add item to inventory or exit? [view/add/exit]  ")
    if ask_user == "view":
        print(inventory)
    elif ask_user == "add":
        items = input("What item do you wish to add to inventory? ")
        quantity = input("What's the quantity of the item? ")
        inventory[items] = quantity
        print(inventory)
    else:
        asking = False
        print("Exiting...")



# 96. Log Parser
# Difficulty: Boss 
# Mission: File server.log contains lines like "ERROR: Fail", "INFO: OK". 
# Count how many "ERROR" lines exist. Skills: Files, Strings, Counting.

# 97. Super Quiz
# Difficulty: Boss Mission: Dict {"Q1": "A1", "Q2": "A2"}. Loop through questions, ask input. Track score. Print final score. Skills: Dicts, Loops, Input.

# 98. CSV Processor
# Difficulty: Boss Mission: Read heroes.csv (Name,Power). Create list of dictionaries [{'Name': 'X', 'Power': 'Y'}]. Filter for Power > 80. Skills: Files, String Parsing, Lists/Dicts.

# 99. Save Game State
# Difficulty: Boss Mission: Dict state = {"level": 5, "items": ["sword"]}. Write this to save.txt in a format you can read back (e.g., JSON or custom format). Skills: Files, Dicts, Serialization logic.

# 100. The Final Report
# Difficulty: Omega Mission:

# Generate a random list of 10 numbers (mission scores).
# Filter out scores < 50.
# Calculate average of remaining.
# Write "Qualified: [List], Average: [Avg]" to final_results.txt. Skills: Random, Lists, Math, Files.