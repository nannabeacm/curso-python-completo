# 02. Identity & Stats: Variables & Data Types

> "I can do this all day." - Captain America

In the superhero world, everyone has stats: Strength, Speed, Intelligence. In Python, we store these stats in **Variables**.

## 1. Variables: The Containers
A variable is a box with a label. You put data inside it.

```python
hero_name = "Tony Stark"
power_level = 9000
is_avenger = True
```

You just created three variables.
- `hero_name` holds text.
- `power_level` holds a number.
- `is_avenger` holds a truth value.

## 2. Data Types: The Superpowers

### Strings (`str`)
Text. Must be wrapped in quotes (`""` or `''`).
```python
weapon = "Mjolnir"
catchphrase = 'I am Groot'
```
**Super Trick:** F-Strings (Formatted Strings).
Combines variables into text.
```python
print(f"{hero_name} wields {weapon}.")
# Output: Tony Stark wields Mjolnir.
```

### Integers (`int`)
Whole numbers. No decimals.
```python
suit_version = 85
infinity_stones = 6
```

### Floats (`float`)
Decimal numbers. Good for precision.
```python
battery_level = 98.5
batmobile_fuel = 45.2
```

### Booleans (`bool`)
True or False. The logic of the universe.
```python
is_worthy = True
is_visiting_from_multiverse = False
```

## 3. Dynamic Typing
Python is smart (like Shuri). You don't need to tell it "This is a number." It figures it out.
```python
enemy = "Thanos"  # It's a string
enemy = 0         # Now it's an int (He was dusted)
```

## 4. Input: The Call to Action
Ask the user for information.
```python
alias = input("What is your superhero name? ")
print(f"Welcome, {alias}.")
```

---
**Next Step:** Controlling the flow of battle.
