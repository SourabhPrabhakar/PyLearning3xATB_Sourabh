def say_hello_arg_default(name="Pramod"):
    print("Hello", name)


say_hello_arg_default()
say_hello_arg_default(name="Rajani")
say_hello_arg_default("Indu")


# Ctrl + Alt  + L - Windowns --Reformat code

def f1(a, b, c):
    print(a, b, c)
    return a + b + c


result = f1(int(input("Enter A: ")), int(input("Enter b:")), int(input("Enter c: ")))
print(result)
