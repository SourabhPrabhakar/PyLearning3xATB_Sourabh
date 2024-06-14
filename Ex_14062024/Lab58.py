# def Allowed_in_Class(name):
#     if(name=="Sourabh"):
#         print("Allowed")
#     else:
#         print("Not Allowed")
# Allowed_in_Class(input("Enter name: "))
# def check_entry(name, allowed_names):
#     if name in allowed_names:
#         print(f"{name} is allowed to enter the class.")
#     else:
#         print(f"{name} is not allowed to enter the class.")
#
#
# allowed_names = ["Alice", "Bob", "Charlie", "David"]
# # check_entry(input("Enter Name: "), allowed_names)
#
# my_list = list(map(int, input("Enter elements separated by space: ").split()))
# print(my_list)

def allowed_to_attend_python_class(name):
    match name:
        case "DELL":
            print("Dell is allowed")
        case "Shubham":
            print("Shubham is allowed")
        case "Pallavi":
            print("Pallavi is allowed")
        case _:
            print("Not Allowed")

allowed_to_attend_python_class(input("Enter the name: "))









