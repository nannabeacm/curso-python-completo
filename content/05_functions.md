# 05. Superpowers: Functions

> "I am Iron Man." (Snap) - Tony Stark

A function is a reusable block of code. It's a superpower you can call whenever you need it. instead of rewriting the same code 10 times, you define it once and call it Key.

## 1. Defining a Function (`def`)
Use `def` to create a superpower.

```python
def summon_mjolnir():
    print("Mjolnir flies into your hand!")

# Calling the function
summon_mjolnir()
```

## 2. Arguments (Parameters)
Powers need targets. You can pass data *into* functions.

```python
def attack(villain):
    print(f"Punching {villain}!")

attack("Thanos")
attack("Joker")
```

### Multiple Arguments
```python
def introduce(hero, alias):
    print(f"I am {hero}, also known as {alias}.")

introduce("Bruce Wayne", "Batman")
```

## 3. Return Values (The Result)
Sometimes a function does math or logic and gives something back.

```python
def calculate_force(mass, acceleration):
    force = mass * acceleration
    return force

hulk_punch = calculate_force(1000, 50)
print(f"Hulk's punch force: {hulk_punch} Newtons")
```

## 4. Default Arguments (Fallback Mode)
You can set default values.

```python
def order_shawarma(quantity=1):
    print(f"Ordering {quantity} Shawarma(s).")

order_shawarma()   # Uses default (1)
order_shawarma(5)  # Uses 5
```

---
**Next Step:** Organizing the team with Data Structures.
