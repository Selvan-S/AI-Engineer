import json
from student_management import Student

students = [
        Student("Cody", 23, 43),
    Student("Selvan", 23, 39),
]
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