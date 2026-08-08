# Week 2 - Activity 3
# Student Information using OOP


class Student:

    def __init__(self, name, age, address, student_id):
        # String: stores the student's full name
        self.name = name

        # Integer: stores the student's age
        self.age = age

        # String: stores the student's address
        self.address = address

        # String: Student ID is stored as text because it may contain
        # leading zeros or letters
        self.student_id = student_id


def main():

    # List: stores Student objects.
    # A list can contain 70 students or any number of students.
    students = []

    print("Student Information System")
    print("--------------------------")

    while True:

        name = input("Enter full name (or 'q' to finish): ")

        if name.lower() == "q":
            break

        # int: converts the user's age input into an integer
        age = int(input("Enter age: "))

        # String: stores the student's address
        address = input("Enter address: ")

        # String: Student ID is kept as text
        student_id = input("Enter Student ID: ")

        # Create a Student object
        student = Student(name, age, address, student_id)

        # Add the Student object to the list
        students.append(student)

        print("Student added.\n")

    # Sort students by age from youngest to oldest
    students.sort(key=lambda student: student.age)

    print("\nStudents sorted by age")
    print("---------------------")

    # Display student information
    for student in students:
        print("Name:", student.name)
        print("Age:", student.age)
        print("Address:", student.address)
        print("Student ID:", student.student_id)
        print("---------------------")


# Start the program
if __name__ == "__main__":
    main()