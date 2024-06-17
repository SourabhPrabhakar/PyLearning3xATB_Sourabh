# Factorial
import math
import math

n = int(input("Enter number: "))
factorial = 1
# result = math.factorial(5)
# print(result)
# range(1,10) #1-9

while n > 0:

    print(n, "*", end=" ")
    factorial = factorial * n
    n = n - 1

print("\n")
for i in range(1, n + 1):
    factorial *= i

print("Factorial is: ", factorial)
