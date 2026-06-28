# Import required modules
import math
import random

# Create empty dictionary to store history
history = {}

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b

# Run menu until user exits
while True:

    print("\n===== Smart Calculator =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # Basic Arithmetic
    if choice == "1":

        try:

            # Take two numbers
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            op = input("Choose Operation: ")

            if op == "1":
                result = add(num1, num2)

            elif op == "2":
                result = subtract(num1, num2)

            elif op == "3":
                result = multiply(num1, num2)

            elif op == "4":
                result = divide(num1, num2)

            else:
                print("Invalid Operation")
                continue

            print("Result =", result)

        except Exception:
            print("Invalid Input")

    # Scientific Calculation
    elif choice == "2":

        number = float(input("Enter Number: "))

        print("Square Root =", math.sqrt(number))
        result = math.sqrt(number)

    # Random Number
    elif choice == "3":

        result = random.randint(1, 100)

        print("Random Number =", result)

    # Store Result
    elif choice == "4":

        key = input("Enter Name to Save Result: ")

        # Store result in dictionary
        history[key] = result

        print("Result Saved Successfully.")

    # View History
    elif choice == "5":

        print("\nSaved Results")

        for key, value in history.items():
            print(key, ":", value)

    # Exit Program
    elif choice == "6":

        print("Program Ended")
        break

    else:

        print("Invalid Choice")