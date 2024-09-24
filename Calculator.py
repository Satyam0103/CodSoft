def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1/2/3/4): ")
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    if choice in operations:
        result = operations[choice](num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid input")
calculator()
