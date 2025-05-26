#Leap Year using If else
Year = int(input("Please enter the year: "))

if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print(f"{Year} is a Leap year")
else:
    print(Year, "is not a Leap Year")

#Leap year using while and function
while True:
    year_input = input("Please enter a year (or type 'exit' to quit): ")

    if year_input.lower() == 'exit':
        print("Goodbye!")
        break

    if not year_input.isdigit():
        print("Invalid input. Please enter a positive number.")
        continue

    Year = int(year_input)

    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        print(f"{Year} is a leap year.\n")
    else:
        print(f"{Year} is not a leap year.\n")