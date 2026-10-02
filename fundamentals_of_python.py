# Calculate Square
def calculate_square(number):
  return number ** 2
result = calculate_square(7)
print(result)

# Calculate Average
def calculate_average(num1, num2, num3):
  return (num1+num2+num3)/3

result_of_average = calculate_average(10,20,30)
print(result_of_average)

#Is Even
def is_even(number):
  return (number % 2) == 0

print(is_even(10))
print(is_even(7))

#Mini Challenge
price = 1000
tax_rate = 0.18
discount_rate = 0.2
def calculate_total(price, tax_rate):
  return price + (price * tax_rate)

def apply_discount(price, discount_rate):
  return price - (price * discount_rate)

def final_price(price, tax_rate, discount_rate):
  total = calculate_total(price, tax_rate)
  price_after_discount_applied = apply_discount(total,discount_rate)
  return price_after_discount_applied

print(final_price(price, tax_rate, discount_rate))

def mystery(x):
    return x * 2

result = mystery(5)
print(result + 3)
  