# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(result)

# except ValueError:
#     print("You didn't enter a valid integer.")

# except ZeroDivisionError:
#     print("You cannot divide by zero.")

def get_temperature():
    try:
        temperature = float(input("Enter temperature: "))

        if temperature < 0:
            raise ValueError("Temperature cannot be negative")

        return temperature

    except ValueError as e:
        print("Invalid input:", e)
        return None
get_temperature(32)
print("---")

def get_number():
    try:
        number = int(input("Enter a number: "))

    except ValueError:
        print("You didn't enter a valid integer.")

    else:
        return number

get_number()
print("---")

def divide(a, b):
    try:
        result = a / b
        print(result)

    except ZeroDivisionError:
        print("You cannot divide by zero.")

divide(10,0)
print("---")

def get_student_value(key):
    student = {
        "name": "Arun",
        "age": 25,
        "course": "Python"
    }
    try:
        get_value =  student[key]
    except KeyError:
        print("Key not found")
    else:
        return get_value

print(get_student_value("name"))
print(get_student_value("dob"))
print("---")

def open_file(file_name):
    try:
        with open(f"./{file_name}", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("The file was not found.")

open_file("hello1.txt")
print("---")

def set_age(age):
    try:
        if(type(age) != int):
            raise ValueError("Age must be number")
        if(age < 0):
            raise ValueError("Age must be above 0")

    except ValueError as e:
        print(e)
    else:
        return age

set_age("3")
set_age(25)
set_age(-5)
print("---")
