# 06. The Roster: Data Structures (Lists, Dicts, Tuples)

> "There was an idea... to bring together a group of remarkable people." - Nick Fury

One variable is a soldier. A **List** is an army. A **Dictionary** is a dossier.

## 1. Lists (The Array)
An ordered collection of items. Mutable (can change).

```python
avengers = ["Iron Man", "Captain America", "Thor", "Hulk"]

print(avengers[0])  # Iron Man
print(avengers[-1]) # Hulk (Last one)

# Adding
avengers.append("Black Widow")

# Removing
avengers.remove("Thor") # He went to space
```

### Slicing (The Multiverse Slice)
Get a sub-group.
```python
original_six = avengers[0:6]
```

## 2. Tuples (The Immutable)
Like lists, but **cannot change**. Use for things that shouldn't change.

```python
infinity_stones = ("Space", "Mind", "Reality", "Power", "Time", "Soul")
# infinity_stones[0] = "Fake Stone" -> ERROR
```

## 3. Dictionaries (The Database)
Key-Value pairs. SHIELD Files.

```python
hero = {
    "name": "Tony Stark",
    "alias": "Iron Man",
    "suit_count": 85,
    "alive": False
}

print(hero["alias"])
hero["alive"] = True # Multiverse logic
```

## 4. Sets (The Unique)
Unordered, unique items. No duplicates.

```python
villains = {"Thanos", "Loki", "Thanos"} 
print(villains) 
# Output: {'Thanos', 'Loki'} (Thanos removed once)
```

---
**Next Module:** Expanding the Universe (Intermediate Python).
