# 4 Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13
# def fibonacci(n):
#     a, b = 0, 1
#     fibonacci_series = [a, b]
#     for _ in range(2, n):
#         a, b = b, a + b
#         fibonacci_series.append(b)
#     return fibonacci_series
#
# Example usage:
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# print(fibonacci(n))
n = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1
print(a, b, end=' ')
for _ in range(2, n):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
