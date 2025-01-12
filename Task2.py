#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
# Simple Calculator in Python

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select a valid operation.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "/"

        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")


calculator()
