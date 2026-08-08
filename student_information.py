# Student class
class Student:

    # Constructor
    def __init__(self, full_name, age, address, student_id):

        # str: stores the student's full name
        self.full_name = full_name

        # int: stores the student's age
        self.age = age

        # str: stores the student's address
        self.address = address

        # str: stores the student's ID
        self.student_id = student_id


# Create an empty list to store students
# list: can store an unknown number of Student objects
students = []

# Ask the user how many students they want to enter
# int: stores the number of students
number_of_students = int(input("Enter number of students: "))


# Get information for each student
for i in range(number_of_students):

    print("\nStudent", i + 1)

    # str: stores the student's full name
    full_name = input("Enter full name: ")

    # int: stores the student's age
    age = int(input("Enter age: "))

    # str: stores the student's address
    address = input("Enter address: ")

    # str: stores the student's ID
    student_id = input("Enter Student ID: ")

    # Create a Student object
    student = Student(full_name, age, address, student_id)

    # Add the Student object to the list
    students.append(student)


# Sort students by age from youngest to oldest
for i in range(len(students)):

    for j in range(i + 1, len(students)):

        if students[i].age > students[j].age:

            # Swap the two students
            students[i], students[j] = students[j], students[i]


# Display the sorted students
print("\nStudents sorted by age")
print("----------------------")

for student in students:

    print("Name:", student.full_name)
    print("Age:", student.age)
    print("Address:", student.address)
    print("Student ID:", student.student_id)
    print()