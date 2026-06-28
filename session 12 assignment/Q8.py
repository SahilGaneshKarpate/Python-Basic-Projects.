# Create Employee class
class Employee:

    # Constructor to initialize data
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name

        # Store department and salary in tuple
        self.details = (department, salary)

    # Function to display employee details
    def show_details(self):
        print("Employee ID :", self.emp_id)
        print("Name :", self.name)
        print("Department :", self.details[0])
        print("Salary :", self.details[1])
        print()


# Create empty dictionary
employees = {}

# Add three employees
for i in range(3):

    # Take employee details
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    # Create employee object
    emp = Employee(emp_id, name, department, salary)

    # Store object in dictionary
    employees[emp_id] = emp

# Display all employee details
print("\nEmployee Details")

for emp in employees.values():
    emp.show_details()