# Exercises: Classes & OOP (The Blueprint)

## Mission 1: The Design
Create `hero_class.py`.
1. Create a class `Superhero`.
2. `__init__` should take `name` and `power`.
3. Method `attack()` should print `"{name} uses {power}!"`.
4. Create an instance for Thor and call `attack()`.

## Mission 2: The Villain (Inheritance)
Create `villain_class.py`.
1. Create a class `Villain` that inherits from `Superhero`.
2. Add a method `evil_laugh()` that prints "Muahaha!".
3. Create an instance for Loki.
4. Make him `attack()` (inherited) and `evil_laugh()` (unique).

## Mission 3: The Bank Account (Encapsulation logic)
Create `bank.py` (Wayne Enterprises).
1. Class `Account`.
2. `__init__` sets `balance = 0`.
3. Method `deposit(amount)`.
4. Method `withdraw(amount)`.
   - Check if `balance >= amount`. If yes, subtract. If no, print "Insufficient Funds".
5. Test it.
