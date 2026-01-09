# 09. Gadgets: Modules & Packages

> "I need a weapon." - Master Chief (Wait, he does).
> "Where is my super suit?" - Frozone

You don't have to build everything from scratch. Python has "Batteries Included". These batteries are **Modules**.

## 1. What is a Module?
A file containing Python code (functions, variables). You `import` it to use it.

## 2. Built-in Modules (The Standard Issue Gear)
Python comes with these. No installation needed.

### `math`
High-level calculation.
```python
import math

print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.14159...
```

### `random`
Chaos magic.
```python
import random

villains = ["Thanos", "Joker", "Magneto"]
choice = random.choice(villains)
print(f"You define {choice}!")
```

### `datetime`
Time travel logic.
```python
import datetime as dt

now = dt.datetime.now()
print(now)
```

## 3. Creating Your Own Module
1. Create `gadgets.py`.
2. Add a function `def batarang(): print("Whoosh")`.
3. In `main.py`:
   ```python
   import gadgets
   gadgets.batarang()
   ```

## 4. PIP (The Black Market / Armory)
To get external libraries (super powerful ones made by other heroes), we use **PIP**.

Terminal command:
```bash
pip install requests
```
This installs the `requests` library from the internet (PyPI).

---
**Next Step:** Creating a Safe House (Virtual Environments).
