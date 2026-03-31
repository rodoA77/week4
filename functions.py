#Functions -  giving a name to a process

def greet():
    print("Hello! Welcome to week 4!")

# Calling the function
greet()
greet()
greet()

# Function with parameters

def greet(name):
    print(f"Hello {name}! Welcome to week 4!")

greet("Rodo")
greet("Claude")
greet("Abelson")
greet("Sussman")


#Function that return a value

def add(a, b, c):
    result = a + b - c
    return result

# Now you can USE the result:

sum = add(5, 10,10)
sustration = add(10, 5, 10)

print(f"5 + 10 - 10 = {sum}")
print(f"10 + 5 - 10 = {sustration}")

# Functions calling other functions

def multiply(a, b):
    return a * b

def square(n):
    return multiply(n, n)

def cube(n):
    return multiply(n, square(n))

print(f"Square of 4:{square(4)}")
print(f"Cube of 3:{cube(3)}")