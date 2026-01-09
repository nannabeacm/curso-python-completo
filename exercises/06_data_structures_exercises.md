# Exercises: Data Structures (The Roster)

## Mission 1: Assemble the Team (Lists)
Create `team.py`.
1. Create a list `avengers = ["Iron Man", "Thor", "Hulk"]`.
2. Append "Captain America".
3. Remove "Thor".
4. Print the first hero in the list (`[0]`).
5. Print the whole list.

## Mission 2: The Inventory (Dictionaries)
Create `inventory.py`.
1. Create a dict `batman_belt`.
2. Add keys: "Batarang" (5), "Smoke Bomb" (10), "Grapple Gun" (1).
3. Print how many Batarangs he has.
4. He used a smoke bomb. Decrease the value by 1. Print the dictionary.

## Mission 3: Unique Powers (Sets)
Create `powers.py`.
`list_of_powers = ["Flight", "Super Strength", "Flight", "Invisibility", "super Strength"]`.
(Note the lowercase 's' in one).
1. Convert this list to a Set to remove duplicates.
2. Print the set.
*Note: Python is case sensitive. "Super Strength" != "super Strength".*

## Mission 4: Tuple Coordinates
Create `coords.py`.
Create a tuple `batcave_loc = (40.7128, -74.0060)`.
Try to change `batcave_loc[0] = 0`.
Catch the error (or watch it crash) to prove it's immutable. Print "Coordinates are locked." after the attempt (hint: use try/except if you know it, otherwise just comment out the line that crashes).
