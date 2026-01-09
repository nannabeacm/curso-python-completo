# 03. The Choice: Control Flow (If, Else, Elif)

> "This is your last chance. After this, there is no turning back." - Morpheus

Heroes make choices.
- If the light is green, go.
- If Thanos snaps, 50% disappear.
- If you are Anakin, join the Dark Side (else, stay Jedi).

In Python, we use `if`, `elif`, and `else` to control the flow of the program.

## 1. The `if` Statement
The gatekeeper. Runs code ONLY if the condition is `True`.

```python
health = 5
if health < 10:
    print("Warning: Shields Critical!")
```

## 2. The `else` Statement
The alternative. Runs if the `if` was `False`.

```python
is_hulk_angry = False

if is_hulk_angry:
    print("HULK SMASH!")
else:
    print("Bruce Banner is calm.")
```

## 3. The `elif` Statement (Else If)
When you have more than two options.

```python
threat_level = "Midnight"

if threat_level == "Low":
    print("Send Happy Hogan.")
elif threat_level == "High":
    print("Send the Avengers.")
elif threat_level == "Midnight":
    print("Send EVERYONE.")
else:
    print("Stay in the Tower.")
```

## 4. Logical Operators (Team Ups)
Combine conditions with `and`, `or`, `not`.

- **and**: Both must be true.
  `if has_shield and has_hammer:` (Captain America in Endgame).
- **or**: At least one is true.
  `if millionaire or god_of_thunder:` (Getting into the VIP party).
- **not**: Reverses the condition.
  `if not is_villain:`

```python
starlord_plan_good = False
iron_man_present = True

if starlord_plan_good or iron_man_present:
    print("We might win.")
else:
    print("We are doomed.")
```

---
**Next Step:** Repeating actions with Loops.
