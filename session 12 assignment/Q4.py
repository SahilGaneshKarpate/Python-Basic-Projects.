# Create Student class
class Student:

    # Constructor
    def __init__(self, name, roll_no):

        # Initialize data members
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Add marks
    def add_mark(self, mark):

        try:

            # Check valid marks
            if mark < 0 or mark > 100:
                raise ValueError

            self.marks_list.append(mark)

        except ValueError:
            print("Invalid Marks")

    # Calculate average
    def get_average(self):

        if len(self.marks_list) == 0:
            return 0

        return sum(self.marks_list) / len(self.marks_list)

    # Display student information
    def display_info(self):

        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())


# Take student details
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")

# Create object
student = Student(name, roll)

# Take 5 marks
for i in range(5):

    mark = float(input("Enter Mark: "))

    student.add_mark(mark)

# Display information
student.display_info()