import calculator
import math_tools

result1 = calculator.add(10, 20)
result2 = calculator.multiply(5, 6)

print(result1)
print(result2)

print(f"Square: {math_tools.square(5)}")
print(f"Cube: {math_tools.cube(3)}")

with open("hello.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("output.txt", "w") as file:
    file.write("I'm\n")
    file.write("Cody.\n")
    file.write("You Got Hacked!\n")