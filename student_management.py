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


students = []

def get_student_details():
    try:
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        marks = int(input("Enter your marks:"))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
    else:
        return Student(name, age, marks)

def add_student(students):
    new_student = get_student_details()

    if new_student is not None:
        students.append(new_student)
        write_students_json(students)
        print("Student added and saved successfully.")
    else:
        print("Student was not added.")

def display_all_students(students):
    if not students:
        print("No Students")
        return

    for student in students:
        student.display_info()
        print(f"Result: {'Pass' if student.has_passed() else 'Fail'}")
        print("---")

def menu():

    while True:
        print("\n--- Student Management System ---")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Exit")
        print("\n")

        choice = input("Enter your choice: ")

        if choice not in("1", "2", "3"):
            print("Invalid choice. Please try again.")
            continue

        if choice == "1":
            print("\n")
            add_student(students)

        elif choice == "2":
            print("\n")
            display_all_students(students)
        else:
            print("\n")
            print("Good bye!")
            break

def write_students_json(students):
    student_data = []

    for student in students:
        student_data.append({
            "name": student.name,
            "age": student.age,
            "marks": student.marks
        })

    with open("students.json", "w") as file:
        json.dump(student_data, file, indent=4)

    print("Completed")

def load_students_data():
    try:
        with open("students.json", "r") as file:
            student_data = json.load(file)

        students = []

        for data in student_data:
            students.append(Student(
                data["name"], data["age"], data["marks"]
            ))

        return students

    except FileNotFoundError:
        return []

if __name__ == "__main__":
    students = load_students_data()
    menu()
    write_students_json(students)