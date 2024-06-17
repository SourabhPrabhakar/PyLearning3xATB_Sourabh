def allowed_to_enter_class(name,password):
    if name=="Sourabh":
        if password=="Yes":
            print("Allowed to ebter the class")
    else:
        print("Not allowed")


allowed_to_enter_class(input("Enter name: "), input("Enter password: "))