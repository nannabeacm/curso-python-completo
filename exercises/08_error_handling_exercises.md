# Exercises: Error Handling (Damage Control)

## Mission 1: The Calculator Safety
Create `safe_calc.py`.
1. Ask user for two numbers.
2. Divide first by second.
3. Wrap it in a `try/except` block to catch `ZeroDivisionError`.
4. Print "Cannot destroy the universe (divide by zero)" if it happens.

## Mission 2: The File Hunter
Create `file_check.py`.
1. Try to open a file named `missing_infinity_stone.txt` in read mode.
2. If it doesn't exist (`FileNotFoundError`), print "Stone not found in this timeline."
3. If it does exist, read it.

## Mission 3: The Input Guard
Create `number_guard.py`.
1. Loop forever (`while True`).
2. Ask user for a number.
3. Try to convert it to `int`.
4. If successful: Print "Thank you" and `break`.
5. If `ValueError`: Print "That is not a number. Try again."
