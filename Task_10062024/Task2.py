#Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(num1 if num1 > num2 else num2)