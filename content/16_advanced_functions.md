# 16. Reality Stone: Decorators & Generators

> "Reality can be whatever I want." - Thanos

Advanced Python features allow you to bend how code works.

## 1. Decorators (Augmenting Power)
A function that wraps another function to give it extra behavior (like the Venom symbiote suit).

```python
def armor(func):
    def wrapper():
        print("Putting on Armor...")
        func()
        print("Armor Disengaged.")
    return wrapper

@armor
def fight():
    print("Punching the bad guy!")

# Calling fight() will now automatically put on armor first.
fight()
```

## 2. Generators (The Time Stone)
Standard functions return everything at once (Lists).
Generators yield one item at a time (Memory efficient).

Imagine Dr. Strange looking at 14 million futures. He looks at them **one by one**, he doesn't load all 14 million into his brain at once.

```python
def infinity_generator():
    stones = ["Space", "Mind", "Reality", "Power", "Time", "Soul"]
    for stone in stones:
        yield stone

gen = infinity_generator()

print(next(gen)) # Space
print(next(gen)) # Mind
```

**Why?**
If you need to process a 10GB file, a Generator reads line-by-line using almost 0 RAM. A List would crash your computer.

---
**Next Step:** The Speed Force (AsyncIO).
