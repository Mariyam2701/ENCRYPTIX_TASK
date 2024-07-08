##TASK 2: CALUCLATOR

header = "CALCULATOR"
print(header.center(90))

while True:
    try:
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    print("\nChoose from the list of operators: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
    choice = input("Enter your choice from 1-4 (or 'end' to quit): ")

    if choice.lower() == "end":
        break

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        print(f"\nThe addition of the 2 numbers is: {num1 + num2}")
    elif choice == 2:
        print(f"\nThe subtraction of the two numbers is: {num1 - num2}")
    elif choice == 3:
        print(f"\nThe multiplication of the two numbers is: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"\nThe division of the two numbers is: {num1 / num2}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

