# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

Year = int(input("Enter the year: "))
if (Year % 4 == 0 and (Year > 0)) and (Year % 100 != 0 or Year % 400 == 0):
    print(Year, "is a Leap Year")
elif (Year > 0):
    print(Year, "is not a Leap year")
else:
    print("Invalid Entry")
