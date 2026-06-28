# Import required modules
import random
import math

# Create empty set
numbers = set()

try:

    # Take 10 numbers from user
    for i in range(10):

        num = int(input("Enter Number: "))

        # Store unique numbers
        numbers.add(num)

    # Convert set into tuple
    number_tuple = tuple(numbers)

    print("Tuple:", number_tuple)

    # Select 3 random numbers
    if len(number_tuple) >= 3:
        print("Random Numbers:",
              random.sample(number_tuple, 3))
    else:
        print("Not enough numbers.")

    # Find sum of tuple
    total = sum(number_tuple)

    # Print square root
    print("Square Root of Sum:",
          math.sqrt(total))

except ValueError:
    print("Please Enter Numbers Only.")