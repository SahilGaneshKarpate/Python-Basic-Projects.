# Function to manage student database
def student_database():

    # Create empty dictionary
    students = {}

    # Run menu until user exits
    while True:

        print("\n----- Student Database -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter Choice: ")

        # Add student
        if choice == "1":

            try:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                # Store student details
                students.update({
                    roll: {
                        "name": name,
                        "age": age,
                        "city": city
                    }
                })

                print("Student Added Successfully.")

            except ValueError:
                print("Invalid Age!")

        # Search student
        elif choice == "2":

            roll = input("Enter Roll Number: ")

            # Get student details
            record = students.get(roll)

            if record:
                print(record)
            else:
                print("Student Not Found.")

        # Display all students
        elif choice == "3":

            if len(students) == 0:
                print("No Records Found.")

            else:
                for roll, details in students.items():
                    print("Roll:", roll)
                    print(details)

        # Exit program
        elif choice == "4":
            print("Program Ended.")
            break

        else:
            print("Invalid Choice.")

# Call function
student_database()