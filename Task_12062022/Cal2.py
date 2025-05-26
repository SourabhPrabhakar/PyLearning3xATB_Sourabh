def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero!"
    return a / b


while True:
    print("\n📘 ===== Simple Python Calculator =====")
    print("1️⃣  Add")
    print("2️⃣  Subtract")
    print("3️⃣  Multiply")
    print("4️⃣  Divide")
    print("5️⃣  Exit")

    choice = input("👉 Enter your choice (1-5): ")

    if choice == '5':
        print("👋 Exiting calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("⚠️ Invalid choice! Please enter a number from 1 to 5.")
        continue

    try:
        num1 = float(input("🔢 Enter first number: "))
        num2 = float(input("🔢 Enter second number: "))
    except ValueError:
        print("❌ Invalid number! Please enter numeric values.")
        continue

    if choice == '1':
        result = add(num1, num2)
        op = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        op = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        op = "*"
    elif choice == '4':
        result = divide(num1, num2)
        op = "/"

    print(f"✅ Result: {num1} {op} {num2} = {result}")

    cont = input("\n🔁 Do you want to perform another calculation? (y/n): ").lower()
    if cont != 'y':
        print("👋Thank you for using the calculator. Goodbye!")
        break
