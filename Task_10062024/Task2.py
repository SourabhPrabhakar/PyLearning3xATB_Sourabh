# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
# import math
number = int(input("Enter a number: "))
print("Square of the number is: ", number ** 2, "\nCube of the number is: ", number ** 3)
# print("Square of the number is: ", int(math.pow(number, 2)),"\nCube of the number is: ", int(math.pow(number,3)))

#Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(num1 if num1 > num2 else num2)