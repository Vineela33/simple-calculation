def main():
    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Input operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform calculation and display result
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error! Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation!")
        return

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
