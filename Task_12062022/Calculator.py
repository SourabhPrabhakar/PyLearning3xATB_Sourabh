def Add(Num1, Num2):
    return Num1 + Num2


def Subtract(Num1, Num2):
    return Num1 - Num2


def Multiplication(Num1, Num2):
    return Num1 * Num2


def Division(Num1, Num2):
    if Num2 == 0:
        return "Invalid num2 value"
    return Num1 / Num2


while True:

    print("\nSelect the Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Close the Calculator")

    Choice = int(input("\nEnter the choice from 1/2/3/4/5: "))

    if Choice == 5:
        print("Good Bye!")
        break

    Num1 = float(input('Enter First Number: '))

    Num2 = float(input('Enter Second Number: '))

    if Choice == 1:
        print("Result is: ", Add(Num1, Num2))
    elif Choice == 2:
        print("Result is: ", Subtract(Num1, Num2))
    elif Choice == 3:
        print("Result is: ", Multiplication(Num1, Num2))
    elif Choice == 4:
        print("Result is: ", Division(Num1, Num2))
    else:
        print("Please choose valid option.")
