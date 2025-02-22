while True:
    operation = input("Decide the operation (+, -, *, /) ***press 'e' to exit***: ")
    
    if operation == 'e':
        print("Exiting...")
        break

    if operation not in ('+', '-', '*', '/'):
        print("Please enter a valid operation.")
        continue

    try:
        print(f"Ok, you want to do the '{operation}' operation.\nNow let's decide two numbers...")
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                continue
            result = num1 / num2

        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numerical values.")
