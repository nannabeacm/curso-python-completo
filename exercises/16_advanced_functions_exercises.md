# Exercises: Decorators & Generators

## Mission 1: The Logger (Decorator)
Create `logger_dec.py`.
1. Create a decorator `log_execution` that prints "Scanning target..." before the function runs and "Target eliminated." after.
2. Apply it to a function `shoot_laser()`.

## Mission 2: The Timer (Decorator)
Create `timer.py`.
1. Create a decorator that measures how long a function takes.
   - `import time`
   - `start = time.time()`
   - call function
   - `end = time.time()`
   - print `end - start`
2. Apply it to a loop that counts to 1,000,000.

## Mission 3: The Factory (Generator)
Create `factory.py`.
1. Create a generator function `droid_factory(n)` that yields "Droid #1", "Droid #2", etc., up to `n`.
2. Use a `for` loop to print the output of `droid_factory(5)`.
