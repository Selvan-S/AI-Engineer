# def calculate():
#     try:
#         first_number = int(input("First number:"))
#         operator = input("Operator (+ - * /):")
#         if operator != "+" and operator != "-" and operator != "*" and operator != "/":
#             raise ValueError("Enter valid supported operator")
#         second_number = int(input("Second number:"))

#         if operator == "+":
#             return first_number + second_number
#         if operator == "-":
#              return first_number - second_number
#         if operator == "*":
#             return first_number * second_number
#         if operator == "/":
#             return first_number / second_number
        
#     except ValueError as e:
#         print(f"Invalid input:", e)
#         return None

#     except ZeroDivisionError:
#         print("Cannot divide by zero.")
#         return None

# print(calculate())

# Interview Friendly design

def calculate(a, operator, b):
    if operator not in {"+", "-", "*", "/"}:
        raise ValueError("Unsupported operator")

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b


def main():
    """
    I'd separate the calculation logic from the user interaction. The calculation function would validate the operator, perform the arithmetic operation, and return the result. I'd allow expected exceptions, such as `ValueError` for invalid input and `ZeroDivisionError` for division by zero, to propagate to the caller. The caller would handle those errors and display an appropriate message. This keeps the calculation function reusable, testable, and easier to maintain.
    """
    try:
        a = float(input("First number: "))
        operator = input("Operator (+ - * /): ").strip()
        b = float(input("Second number: "))

        result = calculate(a, operator, b)
        print(f"Result: {result}")

    except ValueError as e:
        print(f"Invalid input: {e}")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


if __name__ == "__main__":
    main()

