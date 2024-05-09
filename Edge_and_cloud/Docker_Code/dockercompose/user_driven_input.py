# This file will run as a container

def add_two_number(number1,number2):
    return number1 + number2


# main handler

def my_handler():
    try:
        input("Enter yes to move")
        number1 = int(input("Enter the first number : "))
        number2 = int(input("Enter the second number : "))
        result = add_two_number(number1,number2)
        print(f"Sum of {number1} and {number2} is {result}")
    except Exception as e:
        print("Error : Exception in main handler",e)

# Calling the main handler
my_handler()