# subtraction of two numbers
def subtract(x, y):
    return x - y

# addition of two numbers
def add(x, y):
    return x + y


# multiplication of two numbers
def multiply(x, y):
    return x * y


# division of two numbers
def divide(x, y):
    return x / y


print("Welcome to Stanley's plain calculator.")
print("Please select operation:")
print("1.Subtraction Arithmetic")
print("2.Addition Arithmetic")
print("3.Multiplication Arithmetic")
print("4.Division Arithmetic")

while True:
    # user imput digit
    select = input("Enter digit within operation:(1/2/3/4): ")

    # The four options for the user to addition, subtraction, multiplication and division
    if select in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if select == '1':
            print(num1, "-", num2, "=", subtract(num1, num2))


        elif select == '2':
            print(num1, "+", num2, "=", add(num1, num2))

        elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif select == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        # To confirm if the user wants to do another calculation
        while True:
            # main program
            while True:
                answer = str(input('Try again? (y/n): '))

                if answer in ('y', 'n'):
                   break
                print("invalid input.")
            if answer == 'y':
                break
            else:
                print("Goodbye or would you try again?")
                continue