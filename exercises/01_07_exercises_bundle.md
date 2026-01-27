# 01-07 Exercises Bundle: The Avenger's Training Program

Welcome, recruit. To become Earth's Mightiest Programmer, you must complete this gauntlet of 100 exercises. They range from "training wheels" to "Omega Level Threat".

The topics covered are:
1.  **Intro & Setup**
2.  **Variables & Data Types**
3.  **Control Flow (If/Else)**
4.  **Loops (For/While)**
5.  **Functions**
6.  **Data Structures (Lists, Dicts, etc.)**
7.  **File Handling**

---

## Part 1: The Basics (Topics 1-2)
*Focus: Printing, Arithmetic, Variables, Strings, Integers, Input.*

### 01. The First Words
**Difficulty:** Easy
**Mission:** Create a script that prints "I am Iron Man." to the console.
**Example Output:**
```text
I am Iron Man.
```

### 02. Identity Reveal
**Difficulty:** Easy
**Mission:** Create a variable named `hero` and assign it the value "Batman". Print the variable.
**Example Output:**
```text
Batman
```

### 03. The Team Up
**Difficulty:** Easy
**Mission:** Print the string "Avengers" and "Assemble" on the same line, separated by a space.
**Example Output:**
```text
Avengers Assemble
```

### 04. Strength Calculation
**Difficulty:** Easy
**Mission:** Calculate and print the sum of `100` and `55` (representing strength points).
**Example Output:**
```text
155
```

### 05. Speed Test
**Difficulty:** Easy
**Mission:** A speedster runs 500 miles in 2.5 hours. Calculate and print the average speed (miles divided by hours).
**Example Output:**
```text
200.0
```

### 06. True Power
**Difficulty:** Easy
**Mission:** Create a boolean variable `is_invincible` and set it to `False`. Print it.
**Example Output:**
```text
False
```

### 07. Who Are You?
**Difficulty:** Easy
**Mission:** Ask the user for their superhero name using `input()`. Print "Welcome, [Name]".
**Example Output:**
```text
Welcome, Star-Lord
```

### 08. Age of Ultron
**Difficulty:** Easy
**Mission:** Ask the user for the age of Ultron (integer). Print the age plus 1 (next year's age).
**Example Output:**
```text
3
```

### 09. Suit Up (F-Strings)
**Difficulty:** Easy
**Mission:** Use variables `color = "Red"` and `material = "Gold"`. Use an f-string to print "The suit is Red and Gold."
**Example Output:**
```text
The suit is Red and Gold.
```

### 10. Loud Noises
**Difficulty:** Easy
**Mission:** Create a string variable with value "hulk squash". Print it in all uppercase.
**Example Output:**
```text
HULK SQUASH
```

### 11. Secret Identity
**Difficulty:** Easy
**Mission:** The string is "Clark Kent". Replace "Clark" with "Superman" and print the result.
**Example Output:**
```text
Superman Kent
```

### 12. Scanner
**Difficulty:** Easy
**Mission:** Create a variable `power = 9000`. Print the `type` of this variable.
**Example Output:**
```text
<class 'int'>
```

### 13. Team Division
**Difficulty:** Easy
**Mission:** You have 7 heroes. You want to form named teams of 3. Print how many heroes are left over (use modulo `%`).
**Example Output:**
```text
1
```

### 14. Power Scaling
**Difficulty:** Easy
**Mission:** Calculate 2 to the power of 10 (2^10) using Python.
**Example Output:**
```text
1024
```

### 15. Damage Report
**Difficulty:** Medium
**Mission:** Calculate total damage: `(50 * 2) + (100 / 2) - 25`. Print the result (should be a float).
**Example Output:**
```text
125.0
```

---

## Part 2: Controlling the Narrative (Topic 3)
*Focus: Booleans, If/Elif/Else logic, Comparisons.*

### 16. Is it a Bird?
**Difficulty:** Easy
**Mission:** Set `object_seen = "Superman"`. Write an `if` statement checking if `object_seen` is "Superman". If so, print "It's a bird! It's a plane! It's Superman!".
**Example Output:**
```text
It's a bird! It's a plane! It's Superman!
```

### 17. Friend or Foe
**Difficulty:** Easy
**Mission:** Variable `alignment = "Villain"`. If `alignment` is "Hero", print "Save the cat." Else, print "Destroy the world."
**Example Output:**
```text
Destroy the world.
```

### 18. Threat Level
**Difficulty:** Medium
**Mission:** Variable `threat_level` (int).
- If < 5: "street level".
- If >= 5 and < 8: "city level".
- If >= 8: "avengers level".
Test with 9.
**Example Output:**
```text
avengers level
```

### 19. Stronger Avenger
**Difficulty:** Easy
**Mission:** `thor = 100`, `hulk = 110`. Use an `if` to print "Hulk is stronger" if `hulk > thor`.
**Example Output:**
```text
Hulk is stronger
```

### 20. Identity Check
**Difficulty:** Easy
**Mission:** Ask user for a password. If it equals "Cap", print "Access Granted".
**Example Output:**
```text
Access Granted
```

### 21. Worthy
**Difficulty:** Medium
**Mission:** `is_noble = True`, `is_strong = True`. If both are true, print "Worthy of Mjolnir".
**Example Output:**
```text
Worthy of Mjolnir
```

### 22. Any Help?
**Difficulty:** Medium
**Mission:** `has_shield = False`, `has_hammer = True`. If either is true, print "Ready for battle".
**Example Output:**
```text
Ready for battle
```

### 23. Do Not Press
**Difficulty:** Easy
**Mission:** `button_pressed = False`. If NOT button_pressed, print "Safe".
**Example Output:**
```text
Safe
```

### 24. Secret Access
**Difficulty:** Medium
**Mission:** Nested If. Ask for `level` (int). If level > 5, ask for `code` (str). If code is "Alpha", print "Welcome Director Fury". Else print "Access Denied".
**Example Output:**
```text
Welcome Director Fury
```

### 25. The List
**Difficulty:** Easy
**Mission:** `team = "Iron Man, Thor, Hulk"`. Check if "Thor" is `in` the string. Print True/False.
**Example Output:**
```text
True
```

### 26. Truth Serum
**Difficulty:** Medium
**Mission:** Python treats empty strings as False. Create `name = ""`. If `name`: print "Name exists". Else: print "No name provided".
**Example Output:**
```text
No name provided
```

### 27. Suit Status (Ternary)
**Difficulty:** Hard
**Mission:** Assign variable `status` to "Online" if `energy > 0` else "Offline". Assume `energy = 50`. Print `status`.
**Example Output:**
```text
Online
```

### 28. Speed Limit
**Difficulty:** Medium
**Mission:** Input `speed`. If `speed` > 88, print "Time Travel Imminent".
**Example Output:**
```text
Time Travel Imminent
```

### 29. Joker's Game
**Difficulty:** Medium
**Mission:** `card = "Ace"`. If card is NOT "Joker", print "Safe".
**Example Output:**
```text
Safe
```

### 30. Rank Up
**Difficulty:** Medium
**Mission:** `missions_completed` (int). If > 10, print "Pro". If > 5, print "Intermediate". Else "Rookie". (Order matters!). Test with 7.
**Example Output:**
```text
Intermediate
```

---

## Part 3: Repetitive Actions (Topic 4)
*Focus: Loops (For/While), Break/Continue.*

### 31. The Count
**Difficulty:** Easy
**Mission:** Use a for loop to print numbers 1 to 5.
**Example Output:**
```text
1
2
3
4
5
```

### 32. Roll Call
**Difficulty:** Easy
**Mission:** List `heroes = ["Batman", "Superman", "Wonder Woman"]`. Loop through and print each.
**Example Output:**
```text
Batman
Superman
Wonder Woman
```

### 33. Countdown
**Difficulty:** Easy
**Mission:** Use a `while` loop to print countdown from 3 to 1. Then print "Liftoff!".
**Example Output:**
```text
3
2
1
Liftoff!
```

### 34. Total Damage
**Difficulty:** Medium
**Mission:** List `hits = [10, 20, 15]`. Loop to calculate sum. Print total.
**Example Output:**
```text
45
```

### 35. Find the Spy
**Difficulty:** Medium
**Mission:** List `people = ["Hero", "Hero", "Spy", "Hero"]`. Loop through. If "Spy" found, print "Found him!" and `break`.
**Example Output:**
```text
Found him!
```

### 36. Avoid Civilians
**Difficulty:** Medium
**Mission:** Loop 1 to 5. If number is 3, `continue` (skip). Print current number.
**Example Output:**
```text
1
2
4
5
```

### 37. Patrol Route
**Difficulty:** Medium
**Mission:** Use `range(0, 21, 5)` to print checkpoints (0, 5, 10, 15, 20).
**Example Output:**
```text
0
5
10
15
20
```

### 38. Grid Search
**Difficulty:** Hard
**Mission:** Nested loops. Outer loop `x` in 0-1, Inner loop `y` in 0-1. Print `(x, y)`.
**Example Output:**
```text
(0, 0)
(0, 1)
(1, 0)
(1, 1)
```

### 39. Guess the Number
**Difficulty:** Medium
**Mission:** Hardcode `secret = 7`. While `guess` != secret, ask input. If correct, print "Correct". (Assuming user guesses correctly eventually).
**Example Output:**
```text
Guess: 5
Guess: 7
Correct
```

### 40. Rankings
**Difficulty:** Medium
**Mission:** List `racers = ["Flash", "Quicksilver"]`. Use `enumerate` to print "1. Flash", "2. Quicksilver".
**Example Output:**
```text
1. Flash
2. Quicksilver
```

### 41. Decryption
**Difficulty:** Medium
**Mission:** String `code = "S.H.I.E.L.D."`. Loop through characters. If char is not '.', print it on same line (using `end=""`).
**Example Output:**
```text
SHIELD
```

### 42. Training Reps
**Difficulty:** Easy
**Mission:** `reps = 0`. While `reps` < 3, print "Lifting..." and increment `reps`.
**Example Output:**
```text
Lifting...
Lifting...
Lifting...
```

### 43. Power Table
**Difficulty:** Medium
**Mission:** Loop `i` from 1 to 3. Print `i` and `i` squared (i^2).
**Example Output:**
```text
1 1
2 4
3 9
```

### 44. Search Party
**Difficulty:** Medium
**Mission:** Search for "Thanos" in list `["Stark", "Thanos", "Rogers"]`. If found, set a flag variable `found = True`. Print result.
**Example Output:**
```text
Thanos found
```

### 45. Infinity Stones
**Difficulty:** Hard
**Mission:** Count how many times "Stone" appears in `["Stone", "Rock", "Stone", "Gem"]` using a loop (not `.count()`).
**Example Output:**
```text
2
```

---

## Part 4: Reusable Power (Topic 5)
*Focus: Defining functions, Arguments, Return values.*

### 46. Assemble Command
**Difficulty:** Easy
**Mission:** Define function `assemble()` that prints "Avengers Assemble!". Call it.
**Example Output:**
```text
Avengers Assemble!
```

### 47. Greet Hero
**Difficulty:** Easy
**Mission:** Function `greet(name)`. Prints "Hello, [name]". Call with "Peter".
**Example Output:**
```text
Hello, Peter
```

### 48. Calculate Force
**Difficulty:** Medium
**Mission:** Function `force(mass, accel)`. Returns mass * accel. Print result of `force(10, 9.8)`.
**Example Output:**
```text
98.0
```

### 49. Team Report
**Difficulty:** Medium
**Mission:** Function with 3 args: `(leader, heavy, tech)`. Print "Team: [leader], [heavy], [tech]".
**Example Output:**
```text
Team: Cap, Hulk, Iron Man
```

### 50. Sidekick
**Difficulty:** Medium
**Mission:** Function `recruit(hero, sidekick="Robin")`. Call it with just "Batman".
**Example Output:**
```text
Batman and Robin
```

### 51. Named Strategy
**Difficulty:** Medium
**Mission:** Function `plan(a, b)`. Call it using keywords `plan(b="Attack", a="Defend")`. Print `a` then `b`.
**Example Output:**
```text
Defend then Attack
```

### 52. Scope Check
**Difficulty:** Easy
**Mission:** Define global `x = "Global"`. In function, print `x`.
**Example Output:**
```text
Global
```

### 53. Is Alive
**Difficulty:** Medium
**Mission:** Function `check_pulse(bpm)`. Return `True` if bpm > 0, else `False`.
**Example Output:**
```text
True
```

### 54. Documentation
**Difficulty:** Easy
**Mission:** Write a function with a Docstring `"""Prints status."""`. Print `function.__doc__`.
**Example Output:**
```text
Prints status.
```

### 55. Type Hints
**Difficulty:** Medium
**Mission:** Define `def add_power(a: int, b: int) -> int:`. Return sum.
**Example Output:**
```text
(No output needed, just clean code)
```

### 56. Assemble All (*args)
**Difficulty:** Hard
**Mission:** Function `team_up(*args)`. Loop through args and print each. Call with 3 names.
**Example Output:**
```text
Iron Man
Thor
Hulk
```

### 57. Hero Profile (**kwargs)
**Difficulty:** Hard
**Mission:** Function `profile(**kwargs)`. Loop through key, value and print. Call with `name="Stark", armor="Mk85"`.
**Example Output:**
```text
name: Stark
armor: Mk85
```

### 58. Quick Math (Lambda)
**Difficulty:** Medium
**Mission:** Create lambda function `double = lambda x: x * 2`. Print `double(5)`.
**Example Output:**
```text
10
```

### 59. Factorial (Recursion)
**Difficulty:** Hard
**Mission:** Recursive function `fact(n)`. Returns n * fact(n-1). Base case n=1. Calculate fact(5).
**Example Output:**
```text
120
```

### 60. Call for Backup
**Difficulty:** Medium
**Mission:** Define `backup()`. Define `fight()`. `fight` calls `backup`. Call `fight`.
**Example Output:**
```text
Fighting...
Backup arrived!
```

---

## Part 5: Inventory Management (Topic 6)
*Focus: Lists, Dictionaries, Sets, Tuples.*

### 61. The Roster (List)
**Difficulty:** Easy
**Mission:** Create list `heroes = ["Iron Man", "Cap"]`. Print it.
**Example Output:**
```text
['Iron Man', 'Cap']
```

### 62. Who is First?
**Difficulty:** Easy
**Mission:** Print the first item of `heroes`.
**Example Output:**
```text
Iron Man
```

### 63. New Recruit
**Difficulty:** Easy
**Mission:** Append "Spider-Man" to `heroes`. Print list.
**Example Output:**
```text
['Iron Man', 'Cap', 'Spider-Man']
```

### 64. Man Down
**Difficulty:** Easy
**Mission:** Remove "Cap" from list. Print list.
**Example Output:**
```text
['Iron Man', 'Spider-Man']
```

### 65. Civil War (Slicing)
**Difficulty:** Medium
**Mission:** `all_heroes = ["A", "B", "C", "D"]`. Create slice `team_a` with first 2.
**Example Output:**
```text
['A', 'B']
```

### 66. Hero Stats (Dict)
**Difficulty:** Easy
**Mission:** Create dict `stats = {"strength": 100, "speed": 50}`. Print it.
**Example Output:**
```text
{'strength': 100, 'speed': 50}
```

### 67. Check Strength
**Difficulty:** Easy
**Mission:** Print value of "strength" from `stats`.
**Example Output:**
```text
100
```

### 68. Level Up
**Difficulty:** Medium
**Mission:** Change "speed" to 60 in `stats`. Add "intellect": 90.
**Example Output:**
```text
{'strength': 100, 'speed': 60, 'intellect': 90}
```

### 69. Analyze stats
**Difficulty:** Medium
**Mission:** Loop through `stats` and print "Key: Value".
**Example Output:**
```text
strength: 100
speed: 60
...
```

### 70. Unique Powers (Set)
**Difficulty:** Medium
**Mission:** List `["Fly", "Run", "Fly"]`. Convert to set to remove duplicates.
**Example Output:**
```text
{'Fly', 'Run'}
```

### 71. Shared Enemies
**Difficulty:** Hard
**Mission:** `batman_enemies = {"Joker", "Bane"}`. `superman_enemies = {"Lex", "Joker"}`. Find intersection.
**Example Output:**
```text
{'Joker'}
```

### 72. Coordinates (Tuple)
**Difficulty:** Easy
**Mission:** Create tuple `loc = (10, 20)`. Print it.
**Example Output:**
```text
(10, 20)
```

### 73. Unpack Coordinates
**Difficulty:** Medium
**Mission:** Unpack `x, y = loc`. Print x.
**Example Output:**
```text
10
```

### 74. Hero Database
**Difficulty:** Hard
**Mission:** List of dicts. `db = [{"name": "Stark"}, {"name": "Rogers"}]`. Print name of second hero.
**Example Output:**
```text
Rogers
```

### 75. Team Roster (Dict of Lists)
**Difficulty:** Hard
**Mission:** `teams = {"Avengers": ["Thor", "Hulk"], "X-Men": ["Wolverine"]}`. Print first Avenger.
**Example Output:**
```text
Thor
```

---

## Part 6: Archives (Topic 7)
*Focus: Reading/Writing files, Context managers.*

*Note: For these exercises, assume files are in the same directory.*

### 76. Read Mission
**Difficulty:** Easy
**Mission:** Create `mission.txt` manually with text "Save the world". Write python code to open it and read content.
**Example Output:**
```text
Save the world
```

### 77. Read Lines
**Difficulty:** Medium
**Mission:** File has 3 lines. Read using `.readlines()` and print the list.
**Example Output:**
```text
['Line 1\n', 'Line 2\n', 'Line 3']
```

### 78. Log Entry
**Difficulty:** Easy
**Mission:** Write "Mission Success" to a new file `log.txt`.
**Example Output:**
```text
(File created with content "Mission Success")
```

### 79. Append Log
**Difficulty:** Medium
**Mission:** Append "\nReturn to base" to `log.txt`.
**Example Output:**
```text
(File now has two lines)
```

### 80. Safe Open (With)
**Difficulty:** Easy
**Mission:** Use `with open(...)` to read `log.txt`. Print content.
**Example Output:**
```text
Mission Success
Return to base
```

### 81. Parse Data
**Difficulty:** Hard
**Mission:** File `data.txt` has "Stark,100". Read it, split by comma, print name.
**Example Output:**
```text
Stark
```

### 82. Save Team
**Difficulty:** Medium
**Mission:** List `["Hulk", "Thor"]`. Write them to `team.txt`, one per line.
**Example Output:**
```text
(File contains Hulk then Thor on new lines)
```

### 83. Line Count
**Difficulty:** Medium
**Mission:** Count how many lines are in `team.txt`.
**Example Output:**
```text
2
```

### 84. Find Word
**Difficulty:** Hard
**Mission:** Check if "Hulk" is in `team.txt`.
**Example Output:**
```text
True
```

### 85. Copy File
**Difficulty:** Hard
**Mission:** Read `mission.txt`, write content to `backup_mission.txt`.
**Example Output:**
```text
(File duplicated)
```

### 86. Missing File
**Difficulty:** Medium
**Mission:** Try to open `ghost.txt`. Use `try/except FileNotFoundError` to print "File not found".
**Example Output:**
```text
File not found
```

### 87. Sort Names
**Difficulty:** Hard
**Mission:** Read names from file, sort them alphabetically, print them.
**Example Output:**
```text
['Hulk', 'Thor'] (Sorted if input was reversed)
```

### 88. Clean Data
**Difficulty:** Medium
**Mission:** Read line "  Data  \n". Use `.strip()` to clean it.
**Example Output:**
```text
Data
```

### 89. Timestamp Log
**Difficulty:** Hard
**Mission:** Import `datetime`. Write current time + " - Event" to file.
**Example Output:**
```text
2023-10-27 10:00:00 - Event
```

### 90. Config Loader
**Difficulty:** Hard
**Mission:** File: `difficulty=hard`. Read file, split by `=`, print value.
**Example Output:**
```text
hard
```

---

## Part 7: Boss Battles (Mixed Topics)
*Focus: Combining multiple skills.*

### 91. The Inventory System
**Difficulty:** Boss
**Mission:** Create a dictionary inventory. Loop asking user to "add [item]" or "view". If add, update dict count. If view, print all. "exit" to quit.
**Skills:** Dicts, Loops, Input, If/Else.

### 92. Battle Simulator
**Difficulty:** Boss
**Mission:** Hero HP = 100, Enemy HP = 100. Loop while both > 0. Random damage (5-20). Print HP each turn. Declare winner.
**Skills:** Random, Loops, Variables, Math.

### 93. Caesar Cipher
**Difficulty:** Boss
**Mission:** Function `encrypt(text, shift)`. Shift every letter by `shift`. (e.g., A -> B if shift 1). Return encrypted string.
**Skills:** Strings, ASCII/Ord, Functions.

### 94. Data Analyzer
**Difficulty:** Boss
**Mission:** Read `scores.txt` (list of numbers). Calculate average, max, and min. Write results to `report.txt`.
**Skills:** Files, Lists, Math.

### 95. Team Builder
**Difficulty:** Boss
**Mission:** Ask user for 5 hero names. Add to list. Ask to remove one. Print final sorted list.
**Skills:** Inputs, Lists, Methods.

### 96. Log Parser
**Difficulty:** Boss
**Mission:** File `server.log` contains lines like "ERROR: Fail", "INFO: OK". Count how many "ERROR" lines exist.
**Skills:** Files, Strings, Counting.

### 97. Super Quiz
**Difficulty:** Boss
**Mission:** Dict `{"Q1": "A1", "Q2": "A2"}`. Loop through questions, ask input. Track score. Print final score.
**Skills:** Dicts, Loops, Input.

### 98. CSV Processor
**Difficulty:** Boss
**Mission:** Read `heroes.csv` (Name,Power). Create list of dictionaries `[{'Name': 'X', 'Power': 'Y'}]`. Filter for Power > 80.
**Skills:** Files, String Parsing, Lists/Dicts.

### 99. Save Game State
**Difficulty:** Boss
**Mission:** Dict `state = {"level": 5, "items": ["sword"]}`. Write this to `save.txt` in a format you can read back (e.g., JSON or custom format).
**Skills:** Files, Dicts, Serialization logic.

### 100. The Final Report
**Difficulty:** Omega
**Mission:**
1. Generate a random list of 10 numbers (mission scores).
2. Filter out scores < 50.
3. Calculate average of remaining.
4. Write "Qualified: [List], Average: [Avg]" to `final_results.txt`.
**Skills:** Random, Lists, Math, Files.
