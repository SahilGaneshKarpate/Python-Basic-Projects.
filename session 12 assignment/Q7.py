# Create lambda function
square = lambda x: x * x

try:

    # Create empty list
    square_list = []

    # Generate numbers from 1 to 20
    for i in range(1, 21):

        # Store square in list
        square_list.append(square(i))

    print("All Squares:")
    print(square_list)

    print("\nEven Squares:")

    # Print only even squares
    for value in square_list:

        if value % 2 == 0:
            print(value)

except Exception:

    print("Something Went Wrong.")