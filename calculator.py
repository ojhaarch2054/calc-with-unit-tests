#add function
def add():
    try:
        a = int(input("Provide input for addition: "))
        b = int(input("Provide second input for addition: "))
        print(f"Sum of {a} and {b} is {a + b}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

#subtract function
def subtract():
    try:
        a = int(input("Provide input for subtraction: "))
        b = int(input("Provide second input for subtraction: "))
        print(f"Subtraction of {a} and {b} is {a - b}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

#multiplication function
def multiplication():
    try:
        a = int(input("Provide input for multiplication: "))
        b = int(input("Provide second input for multiplication: "))
        print(f"Multiplication of {a} and {b} is {a * b}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

#divide function
def divide():
    try:
        a = int(input("Provide input for division: "))
        b = int(input("Provide second input for division: "))
        if b == 0:
            print("Division by zero is not allowed.")
        if a == 0:
            print("0")
        else:
            print(f"Division of {a} by {b} is {a / b}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

#remainder function
def remainder():
    try:
        a = int(input("Provide input for remainder: "))
        b = int(input("Provide second input for remainder: "))
        if b == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"Remainder of {a} divided by {b} is {a % b}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

#call functions
add()
subtract()
multiplication()
divide()
remainder()