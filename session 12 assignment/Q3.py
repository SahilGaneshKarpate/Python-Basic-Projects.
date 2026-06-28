# Function to manage marks
def manage_marks():

    # Create empty list
    marks = []

    # Take 5 subject marks
    for i in range(5):

        while True:
            try:
                mark = float(input("Enter Subject Marks: "))

                # Add mark to list
                marks.append(mark)
                break

            except ValueError:
                print("Please enter numbers only.")

    # Calculate average
    average = sum(marks) / len(marks)

    print("Average Marks:", average)

    # Print highest marks
    print("Highest Marks:", max(marks))

    # Print lowest marks
    print("Lowest Marks:", min(marks))

    # Sort list in descending order
    marks.sort(reverse=True)

    print("Marks in Descending Order:", marks)


# Call function
manage_marks()