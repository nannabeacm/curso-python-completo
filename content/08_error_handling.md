# 08. Damage Control: Error Handling (Try/Except)

> "Reality is often disappointing." - Thanos

Code fails. Files are missing. Internet goes down. Users type "ten" instead of "10".
If you don't handle errors, your program crashes (The Snap).
If you do, you survive.

## 1. The Structure
- **try**: Attempt this dangerous code.
- **except**: If it explodes, do this instead.

```python
try:
    infinity_stones = 6
    snap_result = infinity_stones / 0 # You can't divide by zero!
except ZeroDivisionError:
    print("You cannot divide by zero. The universe collapses.")
except Exception as e:
    print(f"Unknown alien error: {e}")
```

## 2. Catching Specific Errors
Don't just catch *everything*. Be specific.

- `ValueError`: Wrong type of value (int vs str).
- `FileNotFoundError`: Missing file.
- `TypeError`: Math with strings.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a number! Enter a digit.")
```

## 3. Finally
Runs no matter what. Good for cleanup.

```python
try:
    print("Opening Portal...")
except:
    print("Portal Failed!")
finally:
    print("Closing Portal Emitter.") # Runs even if it failed.
```

---
**Next Step:** Gathering your tools with Modules.
