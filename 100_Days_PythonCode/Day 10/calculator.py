from art import logo
def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
# we DO NOT put parentheses because we do not want to trigger the functions
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary

n1 = 4
n2 = 8
print(operations["*"](4, 8))    # follow the lesson learned from previous session. "*" is equal to multiply in this case
                                        # and it recognises as the function defined in the beginning.

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    while should_accumulate:

        # operation = input("Pick an operation:\n+ \n- \n* \n/")
        # OR
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()    # we can call the function from the inside of the called function, in this case to restart the code
                            # from the beginning

calculator()
