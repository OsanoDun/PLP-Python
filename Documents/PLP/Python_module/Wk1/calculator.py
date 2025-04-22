def calculator():
    print("Welcome to the Basic Calculator!")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero.")
                return
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
