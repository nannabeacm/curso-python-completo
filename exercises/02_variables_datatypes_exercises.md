# Exercises: Variables & Data Types

## Mission 1: Hero Registration Form
Create a script `registration.py`.
Create variables for:
- `hero_name` (String)
- `power_level` (Integer)
- `is_good_guy` (Boolean)

Print them out in a nice format using an **f-string**.
**Target Output:**
```
Hero: Spider-Man
Power Level: 85
Good Guy: True
```

## Mission 2: The Age Calculator
Create `age_calc.py`.
1. variable `birth_year` = 1990 (or your birth year).
2. variable `current_year` = 2025.
3. Calculate `age` by subtracting birth from current.
4. Print: "In 2025, you will be [age] years old."

## Mission 3: Stark Industries Inventory
Tony Stark needs to track his suits.
1. `suits_count` = 50
2. `destroyed_suits` = 15
3. Subtract destroyed from count.
4. Print the result.
5. Then, he builds 10 more (add 10). Print the new total.

## Mission 4: The Interrogation (Input)
Create `interrogation.py`.
Ask the user (using `input()`):
- "Who are you?"
- "Where is the Tesseract?"
Print a dramatic sentence combining their answers.
**Example:**
```
User inputs: Loki, NY
Output: Loki says the Tesseract is in NY. S.H.I.E.L.D. is on the way.
```

## Mission 5: Type Check
Variables can be tricky.
```python
x = "100"
y = 100
```
Print the type of x and y using `type()`.
Try to add them (`x + y`). What happens?
Fix it by converting `x` to an integer (`int(x)`).
