
import json


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def has_passed(self):
        return self.marks >= 40


def get_student_details():
    try:
        name = input("Enter student name: ").strip()
        age = int(input("Enter student age: "))
        marks = int(input("Enter student marks: "))

        if not name:
            print("Name cannot be empty.")
            return None

        if age <= 0:
            print("Age must be positive.")
            return None

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return None

        return Student(name, age, marks)

    except ValueError:
        print("Invalid input. Age and marks must be integers.")
        return None


def write_students_json(students):
    student_data = [
        {
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
        }
        for student in students
    ]

    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(student_data, file, indent=4)


def load_students_data():
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            student_data = json.load(file)

        if not isinstance(student_data, list):
            raise ValueError("Expected a list of student records.")

        students = []

        for data in student_data:
            students.append(
                Student(data["name"], data["age"], data["marks"])
            )

        return students

    except FileNotFoundError:
        return []

    except (json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
        print(f"Could not load student data: {error}")
        print("Please check students.json before continuing.")
        raise


def add_student(students):
    new_student = get_student_details()

    if new_student is None:
        print("Student was not added.")
        return

    students.append(new_student)

    try:
        write_students_json(students)
        print("Student added and saved successfully.")
    except OSError as error:
        print(f"Could not save student data: {error}")
        students.pop()


def display_all_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        student.display_info()
        result = "Pass" if student.has_passed() else "Fail"
        print(f"Result: {result}")
        print("---")


def menu(students):
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_all_students(students)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    students = load_students_data()
    menu(students)
