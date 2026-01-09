# 04. Time Loops: Loops (For & While)

> "Dormammu, I've come to bargain." - Dr. Strange

Superheroes often have to do things repeatedly. Punching minions, running laps around the world, or reliving the same day. In Python, we use **Loops**.

## 1. The `for` Loop (The Iteration)
Used when you know *how many times* you want to repeat, or you want to go through a list.

### Range
The 'range(start, stop)' function generates numbers. 'Stop' is non-inclusive.
```python
# Dr. Strange bargains 5 times
for i in range(5):
    print(f"Dormammu, I've come to bargain (Attempt {i+1})")
```

## 2. The `while` Loop (The Infinite Potential)
Used when you want to repeat *as long as* a condition is true.

```python
health = 100

while health > 0:
    print(f"Still fighting! Health: {health}")
    health = health - 20 # Taking damage

print("Hero Down!")
```

**WARNING:** Be careful of **Infinite Loops**. If the condition never becomes False, your program runs forever.
*(Press `Ctrl + C` in the terminal to kill a rogue loop).*

## 3. Break and Continue
Control the loop from the inside.

- **break**: Stop the loop immediately (Teleport out).
- **continue**: Skip this iteration, go to the next one (Phase through).

```python
for num in range(10):
    if num == 5:
        print("Found the Infinity Stone!")
        break # Mission accomplished, stop searching
    print(f"Searching sector {num}...")
```

---
**Next Step:** Encapsulating power with Functions.
