def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    should_accumulate = True

    num1 = float(input("What is the first number: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Choose an operation: ")
        num2 = float(input("What is the second number: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'q' to quit: ")

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_accumulate = False
            print("\n" * 20)
            calculator()
        else:
            print("Goodbye.")
            break

calculator()
