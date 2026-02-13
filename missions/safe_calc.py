try:
    first_number = float(input("Provide first number for division: "))
    second_number = float(input("Provide second number for division: "))
    result = first_number / second_number
    print(f"Result: {result}")
except ValueError:
    print("Error! Please provide a number!")
except ZeroDivisionError:
    print("Error! Cannot destroy the universe (divide by zero).")