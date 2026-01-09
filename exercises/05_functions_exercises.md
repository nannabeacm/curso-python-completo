# Exercises: Functions (Superpowers)

## Mission 1: The Bat-Signal
Create `bat_signal.py`.
Define a function `light_signal()` that prints:
```text
/  \
|()|    NANANANANANA BATMAN!
\  /
```
Call it 3 times.

## Mission 2: Power Multiplier
Create `multiplier.py`.
Define a function `double_power(level)` that takes a number, multiplies it by 2, and prints the result.
Call it with 50, 100, and 9000.

## Mission 3: The Avenger Assembler (Return)
Create `assembler.py`.
Define `assemble(hero, location)`.
It should **return** a string: `"{hero} is assembling at {location}."`
Store the result in a variable and print it.

## Mission 4: Damage Calculator
Create `damage.py`.
Function `calculate_damage(base_damage, crit_multiplier=2)`.
- If `crit_multiplier` is not provided, use default 2.
- Return `base_damage * crit_multiplier`.

Test cases:
- Normal punch: base 10 (should be 20 crit)
- Super punch: base 50, crit 3 (should be 150)
