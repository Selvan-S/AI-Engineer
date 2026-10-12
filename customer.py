class Customer:
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


customer1 = Customer("Arun", 20, 85)
customer2 = Customer("Priya", 22, 30)

customer1.display_info()
print("---")
customer2.display_info()

print(customer1.has_passed())
print(customer2.has_passed())