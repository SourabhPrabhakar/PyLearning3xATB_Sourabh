# Take 2 int number from user input and add them.
# We need to use the input() function.

# num1 = input("Enter first number : ")
# num2 = input("Enter second number : ")
# result = num1+num2
# print("Result is:", result)
# In above code input() function always returns a string,
# and when you use the + operator with strings, it concatenates them.
# Enter first number : 85
# Enter second number : 55
# result: 8555
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
result = float(num1)+float(num2)
print("Result is :", result)
print(type(int(num1)))
print(type(int(num2)))