from time import sleep

# Operation Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero. You are very dumb. Just for that, you dont get to do any more equations.")
    return a / b

def exponent(a, b):
    return a ** b

# Intro and number of equations a person wants to do.
print("I guess I'll help you do some math. Welcome to the Meh-culator")
sleep(2)
while True:
    try:
        equationCount = int(input("How many equations do you want to do?\n"))
        
        break
    except ValueError:
        print("Please enter an integer")

if equationCount > 10: 
    print("That is way to many, but whatever.")
    sleep(3)

VALID_OPERATIONS_LIST = ["+", "-", "*", "/", "^"]
operationFunctions = [add, subtract, multiply, divide, exponent]

for equationNumber in range(equationCount):

    # What numbers the user wants to use
    while True:
        try:
            number1 = float(input("What is the first number?\n"))
            break
        except ValueError:
            print("Enter a valid number!")

    while True:
        try:
            number2 = float(input("What is the second number?\n"))
            break
        except ValueError:
            print("Enter a valid number!")

    # Asks the user for the operation, makes sure it a correct operation, and then performs the operation
    print("What operation would you like to perform on the two numbers?")
    operation = input("(+, -, *, /, ^): ")

    while operation not in VALID_OPERATIONS_LIST:
        print("Please enter a valid operation")
        operation = input("(+, -, *, /, ^): ")

    operationIndex = VALID_OPERATIONS_LIST.index(operation)

    print(f"The answer is: {operationFunctions[operationIndex](number1, number2):.2f}, are you happy now?")
    sleep(3)

    # Allows user to quit early
    print("If you want to stop being boring, and realized you didn't need this many equations, enter 'q'.")
    quit = input()
    if quit.lower() == "q":
        break