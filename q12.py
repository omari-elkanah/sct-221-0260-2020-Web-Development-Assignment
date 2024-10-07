# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum, difference, product, and quotient
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Check if num2 is not zero to avoid division by zero
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "undefined (cannot divide by zero)"

# Print the results with appropriate labels
print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")