try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("You didn't enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")