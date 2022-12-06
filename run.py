# Addition of two numbers
def add(x, y):
    return x + y


# Subtraction of two numbers
def subtract(x, y):
    return x - y


# Multiplication of two numbers
def multiply(x, y):
    return x * y


# Division of two numbers
def divide(x, y):
    return x / y

print("Welcome to Stanley simple calculator.")
print("Please select operation:")
print("1.Addition Arithmetic")
print("2.Subtract Arithmetic")
print("3.Multiply Arithmetic")
print("4.Division Arithmetic")

while True:
    # User imput
    choice = input("Enter digit within operation:(1/2/3/4): ")

    # The four options for the user to addition, subtraction, multiplication and division
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # To confirm if the user wants to do another calculation
        # The loops breaks with if answer is no
        next_calculation = input("Calculate again? (y/n): ")
        if next_calculation == "n":
            break

    else:
        print("Invalid Input, try again")
