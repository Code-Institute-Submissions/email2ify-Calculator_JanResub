""" The functions of subtraction, addition
    multiplication, division and global scope
"""


def subtract(num1, num2):
    """subtract"""
    result = num1 - num2
    return result


# addition of two numbers


def add(num1, num2):
    """addition"""
    result = num1 + num2
    return result


# multiplication of two numbers


def multiply(num1, num2):
    """""multiplication"""""
    result = num1 * num2
    return result


# division of two numbers


def divide(num1, num2):
    """division"""
    try:
        return (num1 / num2)
    except ZeroDivisionError:
        print("Error: dividing by zero!")

# ------- Global scope-------


def main():
    """function called in the global scope"""
    print("Welcome to Stanley's plain calculator.")
    print("Please select operation:")
    print("1.Subtraction Arithmetic")
    print("2.Addition Arithmetic")
    print("3.Multiplication Arithmetic")
    print("4.Division Arithmetic")

    while True:
        # user imput digit and the four options for the user
        select = input("Enter digit within operation:(1/2/3/4): ")
        # The four options for the user ()
        if select in ('1', '2', '3', '4'):
            while True:
                # try and get 2 numbers
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
        # if not numbers, throw exception
                except Exception:
                    print(
                        "Invalid input, select correct numbers as specified")
                    # Go back to start while loop
                    continue
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
                    answer = str(input('Try again? (y/n): '))
                    if answer in ('y', 'n'):
                        break
                    print("invalid input.")

                if answer == 'y':
                    pass
                else:
                    print("Goodbye and have a nice day.")
                    break
# run


main()
