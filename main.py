# #Basic_Calculator
#
# print("Please select an operation: ")
# print("1: Addition")
# print("2: Subtraction")
# print("3: Multiplication")
# print("4: Division")
#
# operation = input()
#
# if operation == '1':
#     number1 = input("Enter your first number: ")
#     number2 = input("Enter your second number: ")
#     print("The Addition is " + str(int(number1) + int(number2)))
# elif operation == '2':
#     number1 = input("Enter your first number: ")
#     number2 = input("Enter your second number: ")
#     print("The Subtraction is " + str(int(number1) - int(number2)))
# elif operation == '3':
#     number1 = input("Enter your first number: ")
#     number2 = input("Enter your second number: ")
#     print("The Multiplication is" + str(int(number1) * int(number2)))
# elif operation == '4':
#     number1 = input("Enter your first number: ")
#     number2 = input("Enter your second number: ")
#     print("The Division is " + str(int(number1) / int(number2)))
#
# else:
#     print("Invalid Input!!")


# Basic_Calculator


def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


def exit():
    print("Thanks For Exit.. ^_^ ")


print("Please select an operation: ")
print("1: addition")
print("2: subtraction")
print("3: multiplication")
print("4: division")
print("5: exit")

select = int(input(""))
if select == 1:
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter first number: '))
    print(f"The Addition is {addition(number_1, number_2)}")
elif select == 2:
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter first number: '))
    print(f"The Subtraction is {subtraction(number_1, number_2)}")
elif select == 3:
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter first number: '))
    print(f"The Multiplication is {multiplication(number_1, number_2)}")
elif select == 4:
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter first number: '))
    print(f"The Division is {division(number_1, number_2)}")
elif select == 5:
    exit()

else:
    print("Invalid Input")
