Num = int(input("Enter the number: "))

for i in range(1, Num + 1):
    Spaces = ' ' * (Num - i)
    Starts = '*' * (2 * i - 1)
    print(Spaces + Starts)
