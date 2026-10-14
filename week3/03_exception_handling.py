try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

try:
    numerator = float(input("Numerator: "))
    denominator = float(input("Denominator: "))
    result = numerator / denominator
except ValueError:
    print("Enter numeric values only.")
except ZeroDivisionError:
    print("The denominator cannot be zero.")
else:
    print("Result:", result)
