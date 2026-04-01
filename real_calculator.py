# A calculator built entirely from functions
# Each operation is its own abstraction

def add(a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "That is not possible in this universe"
    return a / b

def power(a, b):
    return a ** b

def root(a, b):
    if b == 0:
        return "So now you are trying to invent new math!?"
    return a ** (1/b)

def calculate():
    print("===Calculator===")
    a = float(input("First number: "))
    b = float(input("Second number: "))
    operation = input("Operation (add, substract, multiply, divide, power, root): ")

    if operation == "add":
        print(f"Result: {add(a, b)}")
    elif operation == "subtract":
        print(f"Result: {subtract (a, b)}")
    elif operation == "multiply":
        print(f"Result: {multiply(a, b)}")
    elif operation == "divide":
        print(f"Result: {divide(a, b)}")
    elif operation == "power":
        print(f"Result: {power(a, b)}")
    elif operation == "root":
        print(f"Result: {root(a, b)}")
    else: 
        print("Sorry, but what are you trying to do?")

while True:
    calculate()
    again = input("Calculate again? (yes/no): ")
    if again != "yes":
        print("Goodbye, and thanks for the math!")
        break

